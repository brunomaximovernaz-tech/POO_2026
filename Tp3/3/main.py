from seeder import Seeder

class Main:
    """
    Clase principal que maneja EXCLUSIVAMENTE la interacción con el usuario (impresión y lectura).
    """
    def __init__(self):
        self.mapa = Seeder()

    def mostrarMenu(self):
        print("\n" + "="*40)
        print("        SISTEMA DE MAPA MUNDIAL")
        print("="*40)
        print("1. Buscar Continente y listar sus países")
        print("2. Buscar País y listar sus provincias")
        print("3. Buscar País y listar países limítrofes")
        print("4. Listar todos los países por superficie (descendente)")
        print("5. Comparar superficie de 2 países")
        print("6. Salir")
        print("="*40)
        return input("Seleccione una opción: ")

    def ejecutar(self):
        while True:
            opcion = self.mostrarMenu()
            
            if opcion == '1':
                nombre_continente = input("\nIngrese el nombre del Continente (Ej: America, Europa): ")
                continente = self.mapa.buscarContinente(nombre_continente)
                if continente:
                    print(f"\n>>> Países en {continente.nombre}:")
                    for pais in continente.paises:
                        print(f"  - {pais.nombre}")
                else:
                    print("\n[!] Continente no encontrado.")
                    
            elif opcion == '2':
                nombre_pais = input("\nIngrese el nombre del País: ")
                pais = self.mapa.buscarPais(nombre_pais)
                if pais:
                    print(f"\n>>> Provincias de {pais.nombre}:")
                    if len(pais.provincias) > 0:
                        for prov in pais.provincias:
                            print(f"  - {prov.nombre}")
                    else:
                        print("  [No tiene provincias registradas]")
                else:
                    print("\n[!] País no encontrado.")
                    
            elif opcion == '3':
                nombre_pais = input("\nIngrese el nombre del País: ")
                pais = self.mapa.buscarPais(nombre_pais)
                if pais:
                    print(f"\n>>> Países limítrofes de {pais.nombre}:")
                    if len(pais.limitrofes) > 0:
                        for limitrofe in pais.limitrofes:
                            print(f"  - {limitrofe.nombre}")
                    else:
                        print("  [No tiene países limítrofes registrados]")
                else:
                    print("\n[!] País no encontrado.")
                    
            elif opcion == '4':
                print("\n>>> Países ordenados por superficie (mayor a menor):")
                paises_ordenados = self.mapa.obtenerPaisesOrdenadosPorSuperficie()
                for pais in paises_ordenados:
                    print(f"  - {pais}") 
                    
            elif opcion == '5':
                nombre_pais1 = input("\nIngrese el nombre del primer País: ")
                nombre_pais2 = input("Ingrese el nombre del segundo País: ")
                resultado = self.mapa.compararSuperficie(nombre_pais1, nombre_pais2)
                
                if resultado is None:
                    print("\n[!] Uno o ambos países no fueron encontrados en el sistema.")
                elif resultado is False:
                    print("\n>>> Ambos países tienen la misma superficie.")
                else:
                    print(f"\n>>> El país con mayor superficie es: {resultado.nombre} ({resultado.superficie} km2).")
                    
            elif opcion == '6':
                print("\nSaliendo del programa... ¡Hasta luego!")
                break
                
            else:
                print("\n[!] Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    app = Main()
    app.ejecutar()
