# ─────────────────────────────────────────────────────────────
# TP4 – Punto 3: Ver para creer
# Constructores y la palabra super()
# ─────────────────────────────────────────────────────────────


class Archivo:
    def __init__(self, nombre, pesoEnMB):
        print("Creando Archivo genérico...")
        self.nombre = nombre
        self.pesoEnMB = pesoEnMB


class ArchivoVideo(Archivo):
    def __init__(self, nombre, pesoEnMB, duracionEnSeg):
        super().__init__(nombre, pesoEnMB)
        print("Creando Archivo de Video...")
        self.duracionEnSeg = duracionEnSeg


# ─────────────────────────────────────────────────────────────
# CASO 1: con super() — funciona correctamente
# ─────────────────────────────────────────────────────────────
print("=== CASO 1: instanciación correcta con super() ===")
video = ArchivoVideo("pelicula.mp4", 1450.7, 7200)
print(f"nombre: {video.nombre}")
print(f"pesoEnMB: {video.pesoEnMB}")
print(f"duracionEnSeg: {video.duracionEnSeg}")


# ─────────────────────────────────────────────────────────────
# CASO 2: sin super() — se omite la llamada al constructor
#         de la superclase y los atributos no se inicializan
# ─────────────────────────────────────────────────────────────
print("\n=== CASO 2: sin super() — qué error ocurre ===")

class ArchivoVideoSinSuper(Archivo):
    def __init__(self, nombre, pesoEnMB, duracionEnSeg):
        # super().__init__(nombre, pesoEnMB)  <-- línea omitida
        print("Creando Archivo de Video...")
        self.duracionEnSeg = duracionEnSeg

video2 = ArchivoVideoSinSuper("clip.avi", 200.0, 300)

try:
    print(f"nombre: {video2.nombre}")
except AttributeError as e:
    print(f"AttributeError: {e}")

try:
    print(f"pesoEnMB: {video2.pesoEnMB}")
except AttributeError as e:
    print(f"AttributeError: {e}")

print(f"duracionEnSeg: {video2.duracionEnSeg}")  # este sí existe
