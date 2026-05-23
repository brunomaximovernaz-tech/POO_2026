from continente import Continente
from pais import Pais
from provincia import Provincia

class Seeder:
    """
    Clase encargada de gestionar los datos de la aplicación.
    No contiene NINGÚN print ni input. Toda interacción ocurre en la clase Main.
    """
    def __init__(self):
        self.continentes = []
        self.paises = []
        self.inicializarDatos()

    def inicializarDatos(self):
        # Continentes
        america = Continente("America")
        europa = Continente("Europa")

        self.continentes.append(america)
        self.continentes.append(europa)

        # Paises y Provincias - America
        argentina = Pais("Argentina", "Buenos Aires", 2780400, america)
        america.agregarPais(argentina)
        argentina.agregarProvincia(Provincia("Buenos Aires"))
        argentina.agregarProvincia(Provincia("Cordoba"))
        argentina.agregarProvincia(Provincia("Santa Fe"))

        brasil = Pais("Brasil", "Brasilia", 8515767, america)
        america.agregarPais(brasil)
        brasil.agregarProvincia(Provincia("Sao Paulo"))
        brasil.agregarProvincia(Provincia("Rio de Janeiro"))

        chile = Pais("Chile", "Santiago", 756102, america)
        america.agregarPais(chile)
        chile.agregarProvincia(Provincia("Santiago"))
        chile.agregarProvincia(Provincia("Valparaiso"))

        uruguay = Pais("Uruguay", "Montevideo", 176215, america)
        america.agregarPais(uruguay)
        uruguay.agregarProvincia(Provincia("Montevideo"))
        uruguay.agregarProvincia(Provincia("Maldonado"))

        usa = Pais("Estados Unidos", "Washington D.C.", 9833517, america)
        america.agregarPais(usa)
        usa.agregarProvincia(Provincia("California"))
        usa.agregarProvincia(Provincia("Texas"))

        canada = Pais("Canada", "Ottawa", 9984670, america)
        america.agregarPais(canada)
        canada.agregarProvincia(Provincia("Ontario"))
        canada.agregarProvincia(Provincia("Quebec"))

        # Limites America
        argentina.agregarLimitrofe(brasil)
        argentina.agregarLimitrofe(chile)
        argentina.agregarLimitrofe(uruguay)
        brasil.agregarLimitrofe(argentina)
        brasil.agregarLimitrofe(uruguay)
        chile.agregarLimitrofe(argentina)
        uruguay.agregarLimitrofe(argentina)
        uruguay.agregarLimitrofe(brasil)
        usa.agregarLimitrofe(canada)
        canada.agregarLimitrofe(usa)

        # Paises y Provincias - Europa
        espana = Pais("Espana", "Madrid", 505990, europa)
        europa.agregarPais(espana)
        espana.agregarProvincia(Provincia("Madrid"))
        espana.agregarProvincia(Provincia("Barcelona"))

        francia = Pais("Francia", "Paris", 643801, europa)
        europa.agregarPais(francia)
        francia.agregarProvincia(Provincia("Ile-de-France"))
        francia.agregarProvincia(Provincia("Provenza"))

        alemania = Pais("Alemania", "Berlin", 357022, europa)
        europa.agregarPais(alemania)
        alemania.agregarProvincia(Provincia("Baviera"))
        alemania.agregarProvincia(Provincia("Berlin"))

        italia = Pais("Italia", "Roma", 301340, europa)
        europa.agregarPais(italia)
        italia.agregarProvincia(Provincia("Lacio"))
        italia.agregarProvincia(Provincia("Lombardia"))

        portugal = Pais("Portugal", "Lisboa", 92090, europa)
        europa.agregarPais(portugal)
        portugal.agregarProvincia(Provincia("Lisboa"))
        portugal.agregarProvincia(Provincia("Oporto"))

        # Limites Europa
        espana.agregarLimitrofe(francia)
        espana.agregarLimitrofe(portugal)
        portugal.agregarLimitrofe(espana)
        francia.agregarLimitrofe(espana)
        francia.agregarLimitrofe(alemania)
        francia.agregarLimitrofe(italia)
        alemania.agregarLimitrofe(francia)
        italia.agregarLimitrofe(francia)

        self.paises.extend([argentina, brasil, chile, uruguay, usa, canada, espana, francia, alemania, italia, portugal])

    def buscarContinente(self, nombre):
        """Retorna un objeto Continente si lo encuentra, de lo contrario None."""
        for continente in self.continentes:
            if continente.nombre.lower() == nombre.lower():
                return continente
        return None

    def buscarPais(self, nombre):
        """Retorna un objeto Pais si lo encuentra, de lo contrario None."""
        for pais in self.paises:
            if pais.nombre.lower() == nombre.lower():
                return pais
        return None

    def obtenerPaisesOrdenadosPorSuperficie(self):
        """Retorna una nueva lista de países ordenada de mayor a menor superficie usando POO básica."""
        lista_ordenada = list(self.paises)
        n = len(lista_ordenada)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista_ordenada[j].superficie < lista_ordenada[j+1].superficie:
                    lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
        return lista_ordenada

    def compararSuperficie(self, nombre1, nombre2):
        """
        Retorna el País con mayor superficie.
        Retorna None si falta alguno de los países.
        Retorna False si son iguales.
        """
        pais1 = self.buscarPais(nombre1)
        pais2 = self.buscarPais(nombre2)
        
        if not pais1 or not pais2:
            return None 
            
        if pais1.superficie > pais2.superficie:
            return pais1
        elif pais2.superficie > pais1.superficie:
            return pais2
        else:
            return False
