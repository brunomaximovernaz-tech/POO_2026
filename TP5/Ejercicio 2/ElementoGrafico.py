from Punto import Punto

class ElementoGrafico:
    # Constructor
    def __init__(self, color_hex="", posicion_centro=None, nombre_capa=""):
        self._color_hex = color_hex
        # Si no le pasamos un punto, crea uno por defecto en (0,0)
        self._posicion_centro = posicion_centro if posicion_centro else Punto()
        self._nombre_capa = nombre_capa

    # Getters y Setters
    def get_color_hex(self):
        return self._color_hex

    def set_color_hex(self, color_hex):
        self._color_hex = color_hex

    def get_posicion_centro(self):
        return self._posicion_centro

    def set_posicion_centro(self, posicion_centro):
        self._posicion_centro = posicion_centro

    def get_nombre_capa(self):
        return self._nombre_capa

    def set_nombre_capa(self, nombre_capa):
        self._nombre_capa = nombre_capa

    # Método para actualizar las coordenadas del centro
    def mover_a(self, nuevo_destino):
        self._posicion_centro = nuevo_destino

    # Sobrescritura del método equivalente a toString()
    def __str__(self):
        return f"Capa: {self._nombre_capa} | Color: {self._color_hex} | Centro: {self._posicion_centro}"