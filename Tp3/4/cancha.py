from turno import Turno

class Cancha:
    """
    Clase de dominio/lógica que representa una cancha de fútbol 5.
    Mantiene la lista de turnos y valida reservas sin realizar impresiones en pantalla ni lecturas de teclado.
    """
    def __init__(self, numero: int):
        self.numero = numero
        self.turnos = []

    def reservarTurno(self, t: Turno) -> bool:
        """
        Intenta reservar un turno.
        Retorna True si la reserva es exitosa, False si la hora ya está ocupada.
        """
        for turno in self.turnos:
            if turno.hora == t.hora:
                return False
        self.turnos.append(t)
        return True

    def cancelarTurno(self, hora: int) -> bool:
        """
        Cancela un turno existente para una hora dada.
        Retorna True si se canceló correctamente, False si no existía reserva para esa hora.
        """
        for i in range(len(self.turnos)):
            if self.turnos[i].hora == hora:
                self.turnos.pop(i)
                return True
        return False

    def obtenerTurnoPorHora(self, hora: int):
        """
        Retorna el objeto Turno si la hora está ocupada, o None si está libre.
        """
        for turno in self.turnos:
            if turno.hora == hora:
                return turno
        return None
