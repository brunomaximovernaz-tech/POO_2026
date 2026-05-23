class Pais:
    def __init__(self, nombre, capital, superficie, continente):
        self.nombre = nombre
        self.capital = capital
        self.superficie = superficie
        self.continente = continente
        self.provincias = []
        self.limitrofes = []

    def agregarProvincia(self, provincia):
        self.provincias.append(provincia)

    def agregarLimitrofe(self, pais):
        if pais not in self.limitrofes:
            self.limitrofes.append(pais)

    def __str__(self):
        nombre_continente = self.continente.nombre if self.continente else "Ninguno"
        return f"País: {self.nombre} - Capital: {self.capital} - Superficie: {self.superficie} km2 - Continente: {nombre_continente}"
