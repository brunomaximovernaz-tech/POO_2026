class Turno:
    """
    Clase de entidad que representa un Turno reservado por una persona a una hora específica.
    Cumple con la separación estricta de responsabilidades: no interactúa con el usuario.
    """
    def __init__(self, nombre_persona: str, hora: int):
        self.nombre_persona = nombre_persona
        self.hora = hora
