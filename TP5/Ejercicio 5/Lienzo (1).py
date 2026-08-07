class Lienzo:
    def __init__(self):
        # Creamos una colección (lista) dinámica para guardar los elementos gráficos
        self._elementos = []

    def agregar_elemento(self, elemento):
        self._elementos.append(elemento)

    def get_elementos(self):
        return self._elementos