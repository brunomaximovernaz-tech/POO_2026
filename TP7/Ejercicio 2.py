from abc import ABC, abstractmethod

# 1. Clase Abstracta Base
class Correo(ABC):
    """
    Representa la abstracción de un proveedor de correo.
    Define la interfaz común que deben implementar todas las empresas de logística.
    """
    @abstractmethod
    def calcular_costo(self, peso: float) -> float:
        """
        Método abstracto que cada subclase debe sobrescribir
        con su propia regla de negocio/tarifa.
        """
        pass


# 2. Subclases Concretas (Especializaciones)
class OCA(Correo):
    def calcular_costo(self, peso: float) -> float:
        return peso * 15.0


class FedEx(Correo):
    def calcular_costo(self, peso: float) -> float:
        return (peso * 50.0) + 100.0  # Costo base + aduana


class Andreani(Correo):
    def calcular_costo(self, peso: float) -> float:
        return peso * 20.0


# 3. Clase CalculadoraEnvios Refactorizada
class CalculadoraEnvios:
    """
    Calculadora desacoplada de las implementaciones concretas.
    Aplica Polimorfismo: no le importa qué correo sea, solo que sepa calcular su costo.
    """
    def obtener_costo(self, correo: Correo, peso: float) -> float:
        # Sin ningún if / elif: delegación polimórfica directa
        return correo.calcular_costo(peso)


# ---------------------------------------------------------
# Demostración de Extensibilidad (OCP) y Ejemplo de Uso
# ---------------------------------------------------------

# Para agregar DHL, únicamente creamos una nueva clase sin tocar nada de lo anterior:
class DHL(Correo):
    def calcular_costo(self, peso: float) -> float:
        return (peso * 40.0) + 50.0  # Tarifa específica de DHL


if __name__ == "__main__":
    calculadora = CalculadoraEnvios()
    peso_paquete = 10.0

    correos = [OCA(), FedEx(), Andreani(), DHL()]

    print("=== CÁLCULO DE COSTOS DE ENVÍO (Python) ===")
    for correo in correos:
        nombre_correo = correo.__class__.__name__
        costo = calculadora.obtener_costo(correo, peso_paquete)
        print(f"Costo con {nombre_correo}: ${costo:.2f}")