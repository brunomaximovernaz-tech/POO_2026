class Entero:
    def __init__(self, numero: int):
        self.__numero = numero

    # ── Getter / Setter ──────────────────────────────────────────
    def get_numero(self) -> int:
        return self.__numero

    def set_numero(self, numero: int):
        self.__numero = numero

    # ── Métodos de cálculo ───────────────────────────────────────
    def cuadrado(self) -> int:
        return self.__numero * self.__numero

    def es_par(self) -> bool:
        return self.__numero % 2 == 0

    def es_impar(self) -> bool:
        return not self.es_par()

    def factorial(self) -> int:
        resultado = 1
        for i in range(2, self.__numero + 1):
            resultado *= i
        return resultado

    def es_primo(self) -> bool:
        n = self.__numero
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        divisor = 3
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 2
        return True