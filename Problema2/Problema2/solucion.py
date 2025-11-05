import time
import sys

def generar_coeficientes_pascal(n):

    if n == 0:
        return [1]
    
    # Inicializar con la primera fila del triángulo
    coeficientes = [1]
    
    for i in range(1, n + 1):
        nuevo_coeficiente = [1]  # Primer coeficiente siempre es 1
        
        # Calcular coeficientes intermedios
        for j in range(1, i):
            nuevo_coeficiente.append(coeficientes[j - 1] + coeficientes[j])
        
        nuevo_coeficiente.append(1)  # Último coeficiente siempre es 1
        coeficientes = nuevo_coeficiente
    
    return coeficientes

def mostrar_polinomio(coeficientes):

    n = len(coeficientes) - 1
    terminos = []
    
    for i, coef in enumerate(coeficientes):
        exponente = n - i
        
        if coef == 0:
            continue
            
        if exponente == 0:
            terminos.append(f"{coef}")
        elif exponente == 1:
            if coef == 1:
                terminos.append("x")
            else:
                terminos.append(f"{coef}x")
        else:
            if coef == 1:
                terminos.append(f"x^{exponente}")
            else:
                terminos.append(f"{coef}x^{exponente}")
    
    return " + ".join(terminos)

def calcular_polinomio(coeficientes, x):

    n = len(coeficientes) - 1
    resultado = 0
    pasos = []
    
    print(f"\nCálculo paso a paso para x = {x}:")
    print(f"Polinomio: {mostrar_polinomio(coeficientes)}")
    print("-" * 50)
    
    for i, coef in enumerate(coeficientes):
        exponente = n - i
        termino = coef * (x ** exponente)
        resultado += termino
        
        if exponente == 0:
            pasos.append(f"{coef} × {x}^{exponente} = {coef} × 1 = {termino}")
        else:
            pasos.append(f"{coef} × {x}^{exponente} = {coef} × {x**exponente} = {termino}")
    
    # Mostrar todos los pasos
    for i, paso in enumerate(pasos):
        print(f"Término {i+1}: {paso}")
    
    print("-" * 50)
    print(f"Resultado final: {resultado}")
    print(f"Verificación: ({x} + 1)^{n} = {resultado}")
    
    return resultado

def main():
    try:
        # Leer n del usuario
        n = int(input("Ingrese el valor de n (entero no negativo): "))
        if n < 0:
            print("Error: n debe ser un número entero no negativo")
            return
        
        # Medir tiempo de generación de coeficientes
        inicio_generacion = time.time()
        coeficientes = generar_coeficientes_pascal(n)
        tiempo_generacion = time.time() - inicio_generacion
        
        print(f"\n=== RESULTADOS PARA n = {n} ===")
        print(f"Coeficientes: {coeficientes}")
        print(f"Polinomio: {mostrar_polinomio(coeficientes)}")
        print(f"Tiempo de generación: {tiempo_generacion:.6f} segundos")
        
        # Calcular para un valor específico de x
        x = float(input("\nIngrese el valor de x para calcular el polinomio: "))
        
        inicio_calculo = time.time()
        calcular_polinomio(coeficientes, x)
        tiempo_calculo = time.time() - inicio_calculo
        
        print(f"Tiempo de cálculo: {tiempo_calculo:.6f} segundos")
        
        # Guardar resultados en archivo
        with open(f"resultados_polinomio_n{n}.txt", "w", encoding="utf-8") as archivo:
            archivo.write(f"RESULTADOS PARA (x+1)^{n}\n")
            archivo.write("=" * 50 + "\n")
            archivo.write(f"Coeficientes: {coeficientes}\n")
            archivo.write(f"Polinomio: {mostrar_polinomio(coeficientes)}\n")
            archivo.write(f"Tiempo de generación: {tiempo_generacion:.6f} segundos\n")
            archivo.write(f"Valor calculado para x={x}: {calcular_polinomio(coeficientes, x)}\n")
            archivo.write(f"Tiempo de cálculo: {tiempo_calculo:.6f} segundos\n")
        
        print(f"\nResultados guardados en 'resultados_polinomio_n{n}.txt'")
        
        # Prueba específica para n=100
        if n == 100:
            print(f"\n=== PRUEBA ESPECÍFICA PARA n=100 ===")
            print(f"Número de coeficientes: {len(coeficientes)}")
            print(f"Coeficiente máximo: {max(coeficientes)}")
            
    except ValueError:
        print("Error: Por favor ingrese un número válido")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()