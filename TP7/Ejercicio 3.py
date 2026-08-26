from abc import ABC, abstractmethod

# Interfaces Segregadas (Pequeñas y Cohesivas)
class ICalculable(ABC):
    """Interfaz para correos que permiten calcular costos de envío."""
    @abstractmethod
    def calcular_costo(self, peso: float) -> float:
        pass

class IRastreable(ABC):
    @abstractmethod
    def rastrear_paquete_satelital(self) -> str:
        pass

class IExportable(ABC):
    @abstractmethod
    def generar_reporte_aduana(self) -> None:
        pass


# Subclases Concretas (Implementación a medida)
class CorreoLocalOCA(ICalculable):
    """
    OCA es un correo local, por lo tanto SOLO hereda de ICalculable.
    Ya no está obligado a implementar métodos de aduana o satélite que no utiliza.
    """
    def calcular_costo(self, peso: float) -> float:
        return peso * 15.0


class CorreoInternacionalFedEx(ICalculable, IRastreable, IExportable):
    """
    FedEx es internacional. Utiliza la herencia múltiple de Python
    para implementar todas las interfaces de las operaciones que sí soporta.
    """
    def calcular_costo(self, peso: float) -> float:
        return (peso * 50.0) + 100.0

    def rastrear_paquete_satelital(self) -> str:
        return "Seguimiento satelital activado: Paquete en tránsito."

    def generar_reporte_aduana(self) -> None:
        print("Generando documentos legales para la aduana internacional...")


# Demostración de Uso
if __name__ == "__main__":
    peso_paquete = 10.0

    print("=== PRUEBA DE CORREO LOCAL (OCA) ===")
    oca = CorreoLocalOCA()
    costo_oca = oca.calcular_costo(peso_paquete)
    print(f"Costo envío OCA: ${costo_oca:.2f}")

    print("\n=== PRUEBA DE CORREO INTERNACIONAL (FedEx) ===")
    fedex = CorreoInternacionalFedEx()
    costo_fedex = fedex.calcular_costo(peso_paquete)
    print(f"Costo envío FedEx: ${costo_fedex:.2f}")
    print(fedex.rastrear_paquete_satelital())
    fedex.generar_reporte_aduana()