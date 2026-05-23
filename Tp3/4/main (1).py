from turno import Turno
from cancha import Cancha

def main():
    """
    Clase principal / Controlador de la interfaz de usuario en consola.
    Aquí se maneja TODA la interacción con el usuario (impresiones y lecturas de teclado).
    """
    # 1. Instanciar las 3 canchas
    canchas = [Cancha(1), Cancha(2), Cancha(3)]
    
    # Horarios válidos del complejo (de 14:00 a 23:00 hs, en punto)
    # Como el complejo cierra a las 23:00, los turnos en punto que se pueden reservar
    # son desde las 14:00 hs hasta las 22:00 hs (que finaliza a las 23:00 hs).
    horas_validas = [14, 15, 16, 17, 18, 19, 20, 21, 22]
    
    # 2. Mostrar menú interactivo
    while True:
        print("\n" + "=" * 40)
        print("    SISTEMA DE GESTIÓN DE RESERVAS")
        print("=" * 40)
        print("1. Ver estado actual de las canchas")
        print("2. Registrar una nueva reserva")
        print("3. Cancelar una reserva existente")
        print("4. Salir")
        print("-" * 40)
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            print("\n" + "-" * 55)
            print("             ESTADO ACTUAL DE LAS CANCHAS")
            print("-" * 55)
            # Mostrar la cabecera
            print(f"{'Hora':<10} | {'Cancha 1':<25} | {'Cancha 2':<25} | {'Cancha 3':<25}")
            print("-" * 103)
            
            for hora in horas_validas:
                hora_str = f"{hora:02d}:00 hs"
                estados = []
                for cancha in canchas:
                    turno = cancha.obtenerTurnoPorHora(hora)
                    if turno:
                        estados.append(f"Ocupado ({turno.nombre_persona})")
                    else:
                        estados.append("Libre")
                
                print(f"{hora_str:<10} | {estados[0]:<25} | {estados[1]:<25} | {estados[2]:<25}")
            print("-" * 103)
            
        elif opcion == "2":
            print("\n" + "-" * 40)
            print("           NUEVA RESERVA")
            print("-" * 40)
            print("Canchas disponibles:")
            print("1. Cancha 1 (Fútbol 5)")
            print("2. Cancha 2 (Fútbol 5)")
            print("3. Cancha 3 (Fútbol 5)")
            cancha_sel = input("Seleccione la cancha (1-3): ").strip()
            
            if cancha_sel not in ["1", "2", "3"]:
                print("Error: Selección de cancha inválida.")
                continue
                
            cancha_idx = int(cancha_sel) - 1
            cancha_seleccionada = canchas[cancha_idx]
            
            print(f"\nHorarios permitidos (en punto): {horas_validas}")
            hora_sel = input("Ingrese la hora de la reserva (ej. 17): ").strip()
            
            # Validación de entrada sin usar excepciones (try-except)
            if not hora_sel.isdigit():
                print("Error: La hora debe ser un número entero.")
                continue
                
            hora_int = int(hora_sel)
            if hora_int not in horas_validas:
                print("Error: Hora inválida o fuera del rango de atención (14 a 22 hs en punto).")
                continue
                
            nombre = input("Ingrese el nombre de la persona para la reserva: ").strip()
            if nombre == "":
                print("Error: El nombre no puede estar vacío.")
                continue
                
            # Instanciar el turno
            nuevo_turno = Turno(nombre, hora_int)
            
            # Evaluar el resultado retornado por la Cancha e imprimir el mensaje correspondiente
            exito = cancha_seleccionada.reservarTurno(nuevo_turno)
            if exito:
                print("\n>>> Reserva exitosa <<<")
            else:
                print("\n>>> Error: Turno ocupado <<<")
                
        elif opcion == "3":
            print("\n" + "-" * 40)
            print("         CANCELAR RESERVA")
            print("-" * 40)
            print("Canchas:")
            print("1. Cancha 1 (Fútbol 5)")
            print("2. Cancha 2 (Fútbol 5)")
            print("3. Cancha 3 (Fútbol 5)")
            cancha_sel = input("Seleccione la cancha (1-3): ").strip()
            
            if cancha_sel not in ["1", "2", "3"]:
                print("Error: Selección de cancha inválida.")
                continue
                
            cancha_idx = int(cancha_sel) - 1
            cancha_seleccionada = canchas[cancha_idx]
            
            hora_sel = input("Ingrese la hora del turno a cancelar (ej. 17): ").strip()
            
            # Validación de entrada sin usar excepciones
            if not hora_sel.isdigit():
                print("Error: La hora debe ser un número entero.")
                continue
                
            hora_int = int(hora_sel)
            
            exito = cancha_seleccionada.cancelarTurno(hora_int)
            if exito:
                print("\n>>> Reserva cancelada con éxito <<<")
            else:
                print("\n>>> Error: No existe una reserva a esa hora en la cancha seleccionada <<<")
                
        elif opcion == "4":
            print("\n¡Gracias por utilizar el sistema de reservas del Complejo Deportivo!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
