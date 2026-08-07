import math
from ElementoGrafico import ElementoGrafico

class Elipse(ElementoGrafico):
    """
    Representa una elipse como elemento gráfico.
    Hereda color, posición del centro y capa de ElementoGrafico.
    Sus dimensiones se definen por radioMayor (semi-eje a) y
    radioMenor (semi-eje b).

    Nota: cuando radioMayor == radioMenor, la elipse degenera en una
    circunferencia.
    """

    def __init__(self, radio_mayor=0.0, radio_menor=0.0, color_hex="", posicion_centro=None, nombre_capa=""):
        # Llamamos al constructor de la clase padre para inicializar
        # los atributos heredados (color, centro y capa).
        super().__init__(color_hex, posicion_centro, nombre_capa)
        self._radio_mayor = radio_mayor
        self._radio_menor = radio_menor

    # ── Getters y Setters ──────────────────────────────────────────────────────

    def get_radio_mayor(self):
        return self._radio_mayor

    def set_radio_mayor(self, radio_mayor):
        self._radio_mayor = radio_mayor

    def get_radio_menor(self):
        return self._radio_menor

    def set_radio_menor(self, radio_menor):
        self._radio_menor = radio_menor

    # ── Métodos propios ────────────────────────────────────────────────────────

    def calcularArea(self):
        """
        Devuelve el área de la elipse: π × a × b
        donde a = radioMayor y b = radioMenor.
        """
        return math.pi * self._radio_mayor * self._radio_menor

    def calcularPerimetro(self):
        """
        Devuelve una aproximación del perímetro de la elipse usando
        la fórmula de Ramanujan (primera aproximación):
            P ≈ π × [ 3(a + b) - √((3a + b)(a + 3b)) ]
        Esta es mucho más precisa que la fórmula simple 2π × √((a²+b²)/2)
        para elipses muy elongadas.
        """
        a = self._radio_mayor
        b = self._radio_menor
        return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))

    def escalar(self, factor):
        """
        Escala la elipse multiplicando ambos radios por el factor dado.

        Consideraciones conceptuales sobre el factor:
          - factor > 1  → la elipse crece (ampliación uniforme).
          - 0 < factor < 1 → la elipse se reduce (reducción uniforme).
          - factor = 1  → la elipse no cambia.
          - factor = 0  → ambos radios quedarían en 0, la elipse degeneraría
                          a un punto sin área ni perímetro. En un sistema real
                          debería lanzarse una excepción o ignorarse.
          - factor < 0  → un radio negativo es geométricamente inválido.
                          Podría interpretarse como una reflexión sobre el
                          centro, pero en la práctica debería rechazarse con
                          un error para evitar resultados absurdos en área y
                          perímetro.
        """
        self._radio_mayor *= factor
        self._radio_menor *= factor

    # ── Representación en cadena ───────────────────────────────────────────────

    def __str__(self):
        """
        Devuelve una cadena con los datos de la elipse.
        Invoca a super().__str__() para incluir los atributos heredados
        (capa, color y centro) y luego añade los propios de la subclase.
        """
        info_base = super().__str__()
        return (f"{info_base} | Radio mayor: {self._radio_mayor} "
                f"| Radio menor: {self._radio_menor} "
                f"| Área: {self.calcularArea():.4f} "
                f"| Perímetro ≈ {self.calcularPerimetro():.4f}")
