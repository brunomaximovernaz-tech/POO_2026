from ElementoGrafico import ElementoGrafico

class Rectangulo(ElementoGrafico):
    """
    Representa un rectángulo como elemento gráfico.
    Hereda color, posición del centro y capa de ElementoGrafico.
    Sus dimensiones se definen por ladoMenor y ladoMayor.
    """

    def __init__(self, lado_menor=0.0, lado_mayor=0.0, color_hex="", posicion_centro=None, nombre_capa=""):
        # Llamamos al constructor de la clase padre para inicializar
        # los atributos heredados (color, centro y capa).
        super().__init__(color_hex, posicion_centro, nombre_capa)
        self._lado_menor = lado_menor
        self._lado_mayor = lado_mayor

    # ── Getters y Setters ──────────────────────────────────────────────────────

    def get_lado_menor(self):
        return self._lado_menor

    def set_lado_menor(self, lado_menor):
        self._lado_menor = lado_menor

    def get_lado_mayor(self):
        return self._lado_mayor

    def set_lado_mayor(self, lado_mayor):
        self._lado_mayor = lado_mayor

    # ── Métodos propios ────────────────────────────────────────────────────────

    def calcularArea(self):
        """Devuelve el área del rectángulo: base × altura."""
        return self._lado_menor * self._lado_mayor

    def calcularPerimetro(self):
        """Devuelve el perímetro del rectángulo: 2 × (base + altura)."""
        return 2 * (self._lado_menor + self._lado_mayor)

    def escalar(self, factor):
        """
        Escala el rectángulo multiplicando ambos lados por el factor dado.

        Consideraciones conceptuales sobre el factor:
          - factor > 1  → el rectángulo crece (ampliación).
          - 0 < factor < 1 → el rectángulo se reduce (reducción).
          - factor = 1  → el rectángulo no cambia.
          - factor = 0  → ambos lados quedarían en 0, lo que dejaría de ser
                          un rectángulo válido (degenerado a un punto). En un
                          sistema real debería lanzarse una excepción o
                          ignorarse la operación.
          - factor < 0  → una longitud negativa carece de sentido geométrico.
                          Conceptualmente podría interpretarse como una
                          reflexión, pero en la práctica debería tratarse como
                          un error y rechazarse.
        """
        self._lado_menor *= factor
        self._lado_mayor *= factor

    # ── Representación en cadena ───────────────────────────────────────────────

    def __str__(self):
        """
        Devuelve una cadena con los datos del rectángulo.
        Invoca a super().__str__() para incluir los atributos heredados
        (capa, color y centro) y luego añade los propios de la subclase.
        """
        info_base = super().__str__()
        return (f"{info_base} | Lado menor: {self._lado_menor} "
                f"| Lado mayor: {self._lado_mayor} "
                f"| Área: {self.calcularArea()} "
                f"| Perímetro: {self.calcularPerimetro()}")
