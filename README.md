# Lenguajes-y-compiladores-Moreno-Roxana

# 1- Validador FEN
Valida notación Forsyth-Edwards para ajedrez.
Valida 6 campos FEN,Piezas y tablero válidos, Turno, enroque, al paso, Contadores de movimiento
## Uso
python fen_validator.py "fen_string"
python fen_validator.py --examples
python fen_validator.py  # modo interactivo
## Scripts de Instalación
Python 3.6+
## Ejecutar directamente
python fen_validator.py
## Con argumentos
python fen_validator.py "fen_string"
python fen_validator.py --examples
## Requisitos
Python 3.6+
Sin dependencias externas

# 2- Polinomio y Triangulo de Pascal
Contiene una solución para calcular polinomios utilizando coeficientes de Pascal.
## Uso
Asegúrate de tener Python instalado en tu sistema.
Ejecuta el script `solucion.py` para interactuar con el programa.
Compila `g++ -std=c++17 -O2 solucion.cpp -o pascal` y ejecuta `./pascal`, ingresando n y x.
Corre `python3 comparar.py`. Compara tiempos para n=100 y x=2.0.
## Requisitos
Python 3.6+
Compilador C++: g++ o clang++ (instalado en el sistema)
## Resultados
Los tiempos se miden excluyendo importación/compilación.
Para n=100, Python puede ser más lento 
Los resultados se guardan en `resultados_polinomio_n{n}.txt`

# 3- Validador de Formatos
Identifica notación científica, direcciones IP y correos electrónicos.
## Uso
python validador_formatos.py
## Scripts de Instalación
Python 3.6+
## Ejecutar directamente
python validador_formatos.py
## Requisitos
Python 3.6+
Sin dependencias externas

# 4- Traductor de C
Traduce palabras reservadas de C a español manteniendo la estructura del código.
## Uso
python traductor_c.py
## Scripts de Instalación
Python 3.6+
python traductor_c.py
## Requisitos
Python 3.6+
Sin dependencias externas
