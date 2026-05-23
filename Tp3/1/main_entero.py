from entero import Entero

class Main:
    @staticmethod
    def run():
        numero = int(input("Ingrese un número entero: "))
        entero = Entero(numero)
        print(f"Número ingresado  : {entero.get_numero()}")
        print(f"Cuadrado          : {entero.cuadrado()}")
        ...