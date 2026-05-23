class Empleado:
    """Clase de entidad que representa un empleado.
    NO contiene impresión en consola ni lectura de teclado.
    """
    SALARIO_MINIMO = 279718.0  # Salario Mínimo Vital y Móvil
    def _init_(self, nombre, dni, sueldo):
        self.__nombre = nombre
        self.__dni = dni
        self._sueldo = self._validar_sueldo(sueldo)
    def __validar_sueldo(self, sueldo):
        """Si el sueldo es negativo o menor al salario mínimo,
        asigna automáticamente el salario mínimo."""
        if sueldo < 0 or sueldo < Empleado.SALARIO_MINIMO:
            return Empleado.SALARIO_MINIMO
        return sueldo
    # --- Getters ---
    def get_nombre(self):
        return self.__nombre
    def get_dni(self):
        return self.__dni
    def get_sueldo(self):
        return self.__sueldo
    # --- Setters ---
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_sueldo(self, sueldo):
        self._sueldo = self._validar_sueldo(sueldo)