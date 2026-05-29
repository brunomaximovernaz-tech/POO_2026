# Definimos la clase base (Superclase)
class Motor:
    def __init__(self, tipo_combustible, caballos_fuerza):
        self.tipo_combustible = tipo_combustible
        self.caballos_fuerza = caballos_fuerza

    def encender_motor(self):
        print("El motor está en marcha.")

# Definimos la clase derivada (Subclase)
# AQUÍ ESTÁ EL ERROR: Hacemos que Auto herede de Motor pasándolo entre paréntesis.
class Auto(Motor):
    def __init__(self, marca, modelo, tipo_combustible, caballos_fuerza):
        # Llamamos al constructor de la clase padre (Motor)
        super().__init__(tipo_combustible, caballos_fuerza)
        self.marca = marca
        self.modelo = modelo
        
    def tocar_bocina(self):
        print("¡Beep beep!")

# Instanciamos el objeto
mi_auto = Auto("Toyota", "Corolla", "Nafta", 170)

# Al heredar, el Auto puede usar los métodos del Motor directamente, 
# lo cual conceptualmente es incorrecto.
mi_auto.encender_motor()