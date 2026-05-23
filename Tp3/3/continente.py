class Continente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.paises = []

    def agregarPais(self, pais):
        if pais not in self.paises:
            self.paises.append(pais)

    def __str__(self):
        return f"Continente: {self.nombre}"
