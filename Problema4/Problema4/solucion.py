class TraductorC:
    def __init__(self):
        self.diccionario = [
            {"ingles": "auto", "espanol": "automatico"},
            {"ingles": "break", "espanol": "romper"},
            {"ingles": "case", "espanol": "caso"},
            {"ingles": "char", "espanol": "caracter"},
            {"ingles": "const", "espanol": "constante"},
            {"ingles": "continue", "espanol": "continuar"},
            {"ingles": "default", "espanol": "por_defecto"},
            {"ingles": "do", "espanol": "hacer"},
            {"ingles": "double", "espanol": "doble"},
            {"ingles": "else", "espanol": "si_no"},
            {"ingles": "enum", "espanol": "enumeracion"},
            {"ingles": "extern", "espanol": "externo"},
            {"ingles": "float", "espanol": "flotante"},
            {"ingles": "for", "espanol": "para"},
            {"ingles": "goto", "espanol": "ir_a"},
            {"ingles": "if", "espanol": "si"},
            {"ingles": "int", "espanol": "entero"},
            {"ingles": "long", "espanol": "largo"},
            {"ingles": "register", "espanol": "registro"},
            {"ingles": "return", "espanol": "retornar"},
            {"ingles": "short", "espanol": "corto"},
            {"ingles": "signed", "espanol": "con_signo"},
            {"ingles": "sizeof", "espanol": "tamano_de"},
            {"ingles": "static", "espanol": "estatico"},
            {"ingles": "struct", "espanol": "estructura"},
            {"ingles": "switch", "espanol": "interruptor"},
            {"ingles": "typedef", "espanol": "definir_tipo"},
            {"ingles": "union", "espanol": "union"},
            {"ingles": "unsigned", "espanol": "sin_signo"},
            {"ingles": "void", "espanol": "vacio"},
            {"ingles": "volatile", "espanol": "volatil"},
            {"ingles": "while", "espanol": "mientras"}
        ]

    def es_palabra_reservada(self, palabra):
        for i, item in enumerate(self.diccionario):
            if palabra == item["ingles"]:
                return i
        return -1

    def traducir_codigo_c(self, codigo):
        # Delimitadores comunes en código C
        delimitadores = " \t\n(){}[];,+-/%=&|!<>"
        
        # Lista para almacenar tokens y delimitadores preservados
        tokens = []
        current_token = ""
        
        # Tokenización manual preservando delimitadores
        for char in codigo:
            if char in delimitadores:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(char)
            else:
                current_token += char
        
        # Añadir el último token si existe
        if current_token:
            tokens.append(current_token)

        # Traducir tokens
        resultado = []
        for token in tokens:
            # Si el token es una palabra reservada, traducirla
            if token.strip() and token not in delimitadores:
                indice = self.es_palabra_reservada(token)
                if indice != -1:
                    resultado.append(self.diccionario[indice]["espanol"])
                else:
                    resultado.append(token)
            else:
                # Preservar delimitadores y espacios
                resultado.append(token)

        return ''.join(resultado)

    def problema4(self):
        print("=== TRADUCTOR C A ESPAÑOL ===")
        print("Ejemplo: for(int i=0;i<10;i++) { if(x>5) return 1; }")
        
        codigo = input("Ingrese código C: ").strip()
        
        print("\n--- TRADUCCIÓN ---")
        print(f"Original:  {codigo}")
        print("Traducido: ", end="")
        resultado = self.traducir_codigo_c(codigo)
        print(resultado)
      
        print("- Se mantienen operadores y estructura")
        print("- Solo se traducen palabras reservadas")
    

def main():
    traductor = TraductorC()
    traductor.problema4()

if __name__ == "__main__":
    main()