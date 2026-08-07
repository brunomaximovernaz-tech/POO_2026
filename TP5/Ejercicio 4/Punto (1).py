class Punto:
    # Constructor
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    # Getters y Setters
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    # Sobrescritura para imprimir el punto
    def __str__(self):
        return f"({self._x}, {self._y})"