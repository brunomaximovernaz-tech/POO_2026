class Empresa:
    def __init__(self, nombre_empresa):
        self.__nombre_empresa = nombre_empresa
        self.__empleados = []  # Tu lista de empleados
        
    # ... el resto de tus métodos (get_nombre_empresa, registrar_empleado, etc.) ...
    def get_nombre_empresa(self):
        return self.__nombre_empresa
    def get_empleados(self):
        return list(self.__empleados)  # Devuelve copia para proteger la lista
    def registrar_empleado(self, empleado):
        """Registra un empleado si su DNI no está repetido.
        Retorna True si se registró exitosamente, False si el DNI ya existe.
        """
        for emp in self.__empleados:
            if emp.get_dni() == empleado.get_dni():
                return False
        self.__empleados.append(empleado)
        return True
    def obtener_empleado_mayor_sueldo(self):
        """Devuelve el objeto Empleado que más gana.
        Retorna None si no hay empleados registrados.
        """
        if len(self.__empleados) == 0:
            return None
        mayor = self.__empleados[0]
        for emp in self.__empleados:
            if emp.get_sueldo() > mayor.get_sueldo():
                mayor = emp
        return mayor
    def obtener_sueldo_promedio(self):
        """Devuelve el sueldo promedio de todos los empleados (float).
        Retorna 0.0 si no hay empleados registrados.
        """
        if len(self.__empleados) == 0:
            return 0.0
        suma = 0.0
        for emp in self.__empleados:
            suma += emp.get_sueldo()
        return suma / len(self.__empleados)
    def cantidad_empleados(self):
        """Retorna la cantidad de empleados registrados."""
        return len(self.__empleados)