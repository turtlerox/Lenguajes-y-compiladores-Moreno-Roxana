import os
import sys
import time
import subprocess
import shutil
import importlib.util

def _load_python_module_from_candidates(folder, candidates):
    for fname in candidates:
        path = os.path.join(folder, fname)
        if os.path.isfile(path):
            spec = importlib.util.spec_from_file_location("cmp_module", path)
            mod = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(mod)  # type: ignore
                return mod
            except Exception as e:
                print(f"Error al cargar módulo {path}: {e}")
    return None

def comparar_tiempos():
    """
    Compara los tiempos de ejecución de la implementación Python y la C++.
    Busca archivos en la misma carpeta que este script.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    n = 100
    x = 2.0  # Valor de prueba para x

    print("=== COMPARACIÓN DE TIEMPOS PARA n=100 ===")

    # 1) Cargar funciones Python (intenta varios nombres de archivo/componente)
    py_candidates = ["solucion.py", "coeficientes_pascal.py", "pascal_py.py"]
    mod = _load_python_module_from_candidates(script_dir, py_candidates)
    if mod is None:
        print("No se encontró ningún módulo Python candidato en:", ", ".join(py_candidates))
        print("Coloca el archivo Python con funciones generar_coeficientes_pascal y calcular_polinomio_pasos/ calcular_polinomio en la misma carpeta.")
        return

    # Buscar funciones dentro del módulo cargado
    generar = getattr(mod, "generar_coeficientes_pascal", None)
    calcular_pasos = getattr(mod, "calcular_polinomio_pasos", None)
    calcular_simple = getattr(mod, "calcular_polinomio", None) or getattr(mod, "calcular_polinomio_pasos", None)

    if generar is None or calcular_simple is None:
        print("El módulo cargado no expone las funciones requeridas.")
        print("Se requieren: generar_coeficientes_pascal(y) y calcular_polinomio o calcular_polinomio_pasos.")
        return

    # Ejecutar la versión Python (medir solo ejecución de funciones, no import)
    print("\nEjecutando código Python (funciones importadas)...")
    t0 = time.perf_counter()
    try:
        coef_python = generar(n)
        # intentar llamar a la función de cálculo con x (alguna implementaciones imprimen pasos y retornan resultado)
        resultado_python = calcular_simple(coef_python, x)
    except TypeError:
        # algunas implementaciones pueden esperar int/str; intentar conversión
        resultado_python = calcular_simple(coef_python, float(x))
    except Exception as e:
        print("Error al ejecutar funciones Python:", e)
        return
    t1 = time.perf_counter()
    tiempo_python = t1 - t0
    print(f"Tiempo total Python: {tiempo_python:.6f} segundos")

    # 2) Compilar y ejecutar C++
    print("\nEjecutando código C++...")

    # Buscar el archivo fuente C++
    cpp_candidates = ["solucion.cpp", "coeficientes_pascal.cpp", "pascal.cpp"]
    cpp_src = None
    for c in cpp_candidates:
        p = os.path.join(script_dir, c)
        if os.path.isfile(p):
            cpp_src = p
            break
    if cpp_src is None:
        print("No se encontró fuente C++ en:", ", ".join(cpp_candidates))
        return

    # Detectar g++
    gpp = shutil.which("g++") or shutil.which("clang++")
    if gpp is None:
        print("No se encontró 'g++' ni 'clang++' en PATH. Instala un compilador o añadelo al PATH.")
        return

    exe_name = "pascal.exe" if os.name == "nt" else "pascal"
    exe_path = os.path.join(script_dir, exe_name)

    compile_cmd = [gpp, "-std=c++17", "-O2", cpp_src, "-o", exe_path]
    print("Compilando C++:", " ".join(compile_cmd))
    comp = subprocess.run(compile_cmd, capture_output=True, text=True)
    if comp.returncode != 0:
        print("Error al compilar código C++:")
        print(comp.stderr)
        return

    # Ejecutar binario y medir tiempo de ejecución (excluyendo compilación)
    run_cmd = [exe_path] if os.name == "nt" else [exe_path]
    input_data = f"{n}\n{x}\n"
    t2 = time.perf_counter()
    run = subprocess.run(run_cmd, input=input_data, capture_output=True, text=True)
    t3 = time.perf_counter()
    tiempo_cpp = t3 - t2

    if run.returncode != 0:
        print("Error al ejecutar código C++:")
        print(run.stderr)
        return

    print(f"Tiempo total C++: {tiempo_cpp:.6f} segundos")

    # Mostrar comparación
    print(f"\n=== RESULTADO COMPARATIVO ===")
    print(f"Python: {tiempo_python:.6f} segundos")
    print(f"C++:    {tiempo_cpp:.6f} segundos")
    if tiempo_cpp > 0:
        print(f"Ratio:  {tiempo_python/tiempo_cpp:.2f}x (Python/C++)")
    else:
        print("Tiempo C++ demasiado pequeño para calcular ratio.")

if __name__ == "__main__":
    comparar_tiempos()