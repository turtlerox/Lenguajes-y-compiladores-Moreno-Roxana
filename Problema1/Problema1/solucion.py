import re
import argparse
import sys

def validar_notacion_fen(cadena):

    # Dividir la cadena en campos
    campos = cadena.strip().split()
    
    # Una notación FEN debe tener exactamente 6 campos
    if len(campos) != 6:
        return False, f"Inválido: FEN debe tener 6 campos, se encontraron {len(campos)}"
    
    posicion, turno, enroque, al_paso, medio_mov, num_mov = campos
    
    # Validar la posición de las piezas (campo 1)
    filas = posicion.split('/')
    
    # Debe haber exactamente 8 filas
    if len(filas) != 8:
        return False, f"Inválido: Debe haber 8 filas, se encontraron {len(filas)}"
    
    # Piezas válidas: K Q R B N P (blancas) k q r b n p (negras)
    piezas_validas = set('KQRBNPkqrbnp12345678')
    
    for i, fila in enumerate(filas, 1):
        # Verificar que solo contenga caracteres válidos
        if not all(c in piezas_validas for c in fila):
            return False, f"Inválido: Fila {i} contiene caracteres inválidos"
        
        # Calcular el número de casillas en esta fila
        casillas = 0
        for c in fila:
            if c.isdigit():
                casillas += int(c)
            else:
                casillas += 1
        
        # Cada fila debe tener exactamente 8 casillas
        if casillas != 8:
            return False, f"Inválido: Fila {i} tiene {casillas} casillas, debe tener 8"
    
    # Validar el turno activo (campo 2)
    if turno not in ['w', 'b']:
        return False, f"Inválido: Turno debe ser 'w' o 'b', se encontró '{turno}'"
    
    # Validar el enroque (campo 3)
    if enroque != '-':
        # Solo puede contener K, Q, k, q (sin repeticiones)
        if not re.match(r'^[KQkq]{1,4}$', enroque):
            return False, f"Inválido: Enroque inválido '{enroque}'"
        
        # Verificar que no haya letras repetidas
        if len(enroque) != len(set(enroque)):
            return False, "Inválido: Enroque tiene letras duplicadas"
        
        # Verificar orden correcto (K antes de Q para blancas, k antes de q para negras)
        if 'Q' in enroque and 'K' in enroque:
            if enroque.index('Q') < enroque.index('K'):
                return False, "Inválido: Orden de enroque incorrecto (K debe ir antes de Q)"
        if 'q' in enroque and 'k' in enroque:
            if enroque.index('q') < enroque.index('k'):
                return False, "Inválido: Orden de enroque incorrecto (k debe ir antes de q)"
    
    # Validar casilla al paso (campo 4)
    if al_paso != '-':
        # Debe ser una casilla válida en fila 3 o 6 (formato: letra a-h + número 3 o 6)
        if not re.match(r'^[a-h][36]$', al_paso):
            return False, f"Inválido: Casilla al paso '{al_paso}' inválida (debe ser a-h + 3 o 6)"
    
    # Validar contador de medio movimientos (campo 5)
    try:
        medio_movimientos = int(medio_mov)
        if medio_movimientos < 0:
            return False, "Inválido: Contador de medio movimientos debe ser >= 0"
    except ValueError:
        return False, f"Inváli: '{medio_mov}' no es un número válido para medio movimientos"
    
    # Validar número de movimiento completo (campo 6)
    try:
        num_movimiento = int(num_mov)
        if num_movimiento < 1:
            return False, "Inválido: Número de movimiento debe ser >= 1"
    except ValueError:
        return False, f"Inválido: '{num_mov}' no es un número válido para movimiento completo"
    
    # Si pasa todas las validaciones
    return True, "✓ Notación FEN válida"

def main():
    print("=" * 60)
    print("VALIDADOR DE NOTACIÓN FEN (Forsyth-Edwards Notation)")
    print("=" * 60)
    print()
    
    # Ejemplos de prueba
    ejemplos = [
        # FEN válido - posición inicial
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        
        # FEN válido - posición intermedia
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
        
        # FEN inválido - solo 5 campos
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -",
        
        # FEN inválido - 9 casillas en una fila
        "rnbqkbnr/pppppppp/9/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        
        # FEN inválido - turno inválido
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR x KQkq - 0 1",
        
        # FEN inválido - casilla al paso incorrecta
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq e5 0 1",
    ]
    
    for i, fen in enumerate(ejemplos, 1):
        print(f"Ejemplo {i}:")
        print(f"Cadena: {fen}")
        
        es_valido, mensaje = validar_notacion_fen(fen)
        
        print(f"Resultado: {mensaje}")
        
        print("-" * 60)
        print()
    
    # Probar cadena personalizada
    print("\nPrueba tu propia cadena FEN:")
    print("(Presiona Enter sin escribir nada para salir)")
    print()
    
    try:
        while True:
            cadena_usuario = input("Ingresa una cadena FEN: ").strip()
            
            if not cadena_usuario:
                print("\n¡Hasta luego!")
                break
            
            es_valido, mensaje = validar_notacion_fen(cadena_usuario)
            print(f"\n{mensaje}\n")
    except KeyboardInterrupt:
        print("\n\nInterrumpido por el usuario. Saliendo.")
        sys.exit(0)

def cli():
    parser = argparse.ArgumentParser(description="Validador de notación FEN")
    parser.add_argument("fen", nargs="?", help="Cadena FEN a validar")
    parser.add_argument("--examples", action="store_true", help="Mostrar y validar ejemplos")
    args = parser.parse_args()
    
    if args.examples:
        main()
        return
    
    if args.fen:
        valido, mensaje = validar_notacion_fen(args.fen)
        print(mensaje)
        sys.exit(0 if valido else 2)
    
    # Si no hay args, entrar en modo interactivo
    main()

if __name__ == "__main__":
    cli()