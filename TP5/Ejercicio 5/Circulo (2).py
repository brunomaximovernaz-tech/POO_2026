from Elipse import Elipse

class Circulo(Elipse):
    """
    Representa un círculo. Hereda de Elipse, pero garantiza 
    que sus radios mayor y menor sean siempre iguales.
    """

    def __init__(self, radio=0.0, color_hex="", posicion_centro=None, nombre_capa=""):
        # Llamamos a super() pasando el mismo valor para radio_mayor y radio_menor
        super().__init__(radio, radio, color_hex, posicion_centro, nombre_capa)

    # ── Sobrescritura de Setters ───────────────────────────────────────────────
    # Si modifican un radio, actualizamos ambos para no deformar el círculo

    def set_radio_mayor(self, radio):
        super().set_radio_mayor(radio)
        super().set_radio_menor(radio)

    def set_radio_menor(self, radio):
        super().set_radio_mayor(radio)
        super().set_radio_menor(radio)

    def __str__(self):
        return f"[CIRCULO] {super().__str__()}"