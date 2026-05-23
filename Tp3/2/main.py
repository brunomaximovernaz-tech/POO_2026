from empleado import Empleado
from empresa import Empresa

class Main:
    """Clase principal que maneja TODA la interacción con el usuario.
    Es la ÚNICA clase que usa print() e input().
    """

    def __init__(self):
        self.__empresa = Empresa("Mi Empresa S.A.")

    def mostrar_menu(self):
        print("\n" + "=" * 50)
        print("    GESTIÓN DE EMPLEADOS - " + self.__empresa.get_nombre_empresa())
        print("=" * 50)
        print("1. Registrar nuevo empleado")
        print("2. Mostrar empleado que más gana")
        print("3. Mostrar sueldo promedio")
        print("4. Listar todos los empleados")
        print("5. Salir")
        print("-" * 50)

    def leer_opcion(self):
        opcion = input("Seleccione una opción: ")
        return opcion

    def registrar_empleado(self):
        print("\n--- Registrar Nuevo Empleado ---")
        nombre = input("Ingrese el nombre del empleado: ")
        dni = input("Ingrese el DNI del empleado: ")
        sueldo_texto = input("Ingrese el sueldo del empleado: ")
        sueldo = float(sueldo_texto)
        
        nuevo_empleado = Empleado(nombre, dni, sueldo)
        
        # Informar si el sueldo fue ajustado al mínimo
        if sueldo < Empleado.SALARIO_MINIMO:
            print("AVISO: El sueldo ingresado es menor al Salario Mínimo Vital y Móvil.")
            print("Se asignó automáticamente el salario mínimo: $" + str(Empleado.SALARIO_MINIMO))
        
        registrado = self.__empresa.registrar_empleado(nuevo_empleado)
        if registrado:
            print("Empleado '" + nuevo_empleado.get_nombre() + "' registrado exitosamente.")
        else:
            print("ERROR: Ya existe un empleado con el DNI " + dni + ". No se registró.")

    def mostrar_empleado_mayor_sueldo(self):
        print("\n--- Empleado con Mayor Sueldo ---")
        empleado = self.__empresa.obtener_empleado_mayor_sueldo()
        if empleado is None:
            print("No hay empleados registrados.")
        else:
            print("Nombre: " + empleado.get_nombre())
            print("DNI:    " + empleado.get_dni())
            print("Sueldo: $" + str(empleado.get_sueldo()))

    def mostrar_sueldo_promedio(self):
        print("\n--- Sueldo Promedio ---")
        if self.__empresa.cantidad_empleados() == 0:
            print("No hay empleados registrados.")
        else:
            promedio = self.__empresa.obtener_sueldo_promedio()
            print("El sueldo promedio de los " + str(self.__empresa.cantidad_empleados()) +
                  " empleado(s) es: $" + str(round(promedio, 2)))

    def listar_empleados(self):
        print("\n--- Lista de Empleados ---")
        empleados = self.__empresa.get_empleados()
        if len(empleados) == 0:
            print("No hay empleados registrados.")
        else:
            print("{:<5} {:<25} {:<15} {:<15}".format("N°", "Nombre", "DNI", "Sueldo"))
            print("-" * 60)
            numero = 1
            for emp in empleados:
                print("{:<5} {:<25} {:<15} ${:<14}".format(
                    numero,
                    emp.get_nombre(),
                    emp.get_dni(),
                    str(emp.get_sueldo())
                ))
                numero += 1
            print("-" * 60)
            print("Total de empleados: " + str(len(empleados)))

    def ejecutar(self):
        """Bucle principal de la aplicación."""
        print("\nBienvenido al Sistema de Gestión de Empleados")
        print("Salario Mínimo Vital y Móvil vigente: $" + str(Empleado.SALARIO_MINIMO))
        while True:
            self.mostrar_menu()
            opcion = self.leer_opcion()
            if opcion == "1":
                self.registrar_empleado()
            elif opcion == "2":
                self.mostrar_empleado_mayor_sueldo()
            elif opcion == "3":
                self.mostrar_sueldo_promedio()
            elif opcion == "4":
                self.listar_empleados()
            elif opcion == "5":
                print("\nGracias por usar el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

# --- Punto de entrada ---
if __name__ == "__main__":
    app = Main()
    app.ejecutar()