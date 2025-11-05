import re

class Validador:
    # Método para validar notación científica
    def es_notacion_cientifica(self, cadena):
        patron_NC = r'^[-+]?[0-9]*\.?[0-9]+[eE][-+]?[0-9]+$'
        return re.fullmatch(patron_NC, cadena) is not None

    # Método para validar dirección IP
    def es_direccion_ip(self, cadena):
        patron_IP = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return re.fullmatch(patron_IP, cadena) is not None

    # Método para validar correo electrónico
    def es_correo_electronico(self, cadena):
        patron_CE = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.fullmatch(patron_CE, cadena) is not None

    # Método principal que determina el formato
    def determinar_formato(self, cadena):
        if self.es_correo_electronico(cadena):
            return "Correo electrónico"
        elif self.es_direccion_ip(cadena):
            return "Dirección IP"
        elif self.es_notacion_cientifica(cadena):
            return "Notación científica"
        else:
            return "Formato desconocido"


def main():
    validador = Validador()

    print("=== IDENTIFICADOR DE FORMATOS ===")
    print("Formatos reconocidos:")
    print("- Notación científica (ej: 1.54e10, -4.56E-5)")
    print("- Dirección IP (ej: 192.168.1.1, 10.0.0.255)")
    print("- Correo electrónico (ej: nombredeusuario@dominio.com)")
    print("==================================")

    while True:
        cadena = input("\nIngrese una cadena (o 'salir' para terminar): ")

        if cadena.lower() == "salir":
            break

        if not cadena.strip():
            print("Por favor, ingrese una cadena válida.")
            continue

        formato = validador.determinar_formato(cadena)
        print(f'La cadena "{cadena}" es de formato: {formato}')

if __name__ == "__main__":
    main()
