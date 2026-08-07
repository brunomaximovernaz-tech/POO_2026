from Rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    """
    Representa un cuadrado. Hereda de Rectángulo, pero garantiza 
    que sus lados se mantengan siempre iguales.
    """

    def __init__(self, lado=0.0, color_hex="", posicion_centro=None, nombre_capa=""):
        # Llamamos a super() pasando el mismo valor para lado_menor y lado_mayor[cite: 5]
        super().__init__(lado, lado, color_hex, posicion_centro, nombre_capa)

    # ── Sobrescritura de Setters ───────────────────────────────────────────────
    # Si modifican un lado, actualizamos ambos para no deformar el cuadrado

    def set_lado_menor(self, lado):
        super().set_lado_menor(lado)
        super().set_lado_mayor(lado)

    def set_lado_mayor(self, lado):
        super().set_lado_menor(lado)
        super().set_lado_mayor(lado)

    # No hace falta sobrescribir calcularArea() ni calcularPerimetro() porque 
    # heredan la lógica matemática perfecta del rectángulo[cite: 5].
    
    def __str__(self):
        # Reutilizamos el str de Rectangulo pero podemos agregarle un indicativo
        return f"[CUADRADO] {super().__str__()}"