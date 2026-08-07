from Punto import Punto
from Rectangulo import Rectangulo
from Elipse import Elipse
from Cuadrado import Cuadrado
from Circulo import Circulo
from Lienzo import Lienzo

# 1. Instanciar el Lienzo
mi_lienzo = Lienzo()

# 2. Instanciar varias figuras
rect = Rectangulo(lado_menor=10, lado_mayor=20, color_hex="#FFFFFF", nombre_capa="Fondo")
elipse = Elipse(radio_mayor=15, radio_menor=8, color_hex="#FF0000", nombre_capa="Ojo")
cuad = Cuadrado(lado=15, color_hex="#00FF00", nombre_capa="Caja")
circ = Circulo(radio=10, color_hex="#0000FF", nombre_capa="Rueda")

# 3. Agregarlas a la colección del Lienzo
mi_lienzo.agregar_elemento(rect)
mi_lienzo.agregar_elemento(elipse)
mi_lienzo.agregar_elemento(cuad)
mi_lienzo.agregar_elemento(circ)

# 4. El Bucle modificado para el Ejercicio 5
area_total = 0
punto_origen = Punto(0, 0)

for elemento in mi_lienzo.get_elementos():
    # Cambiarlos todos al color "#808080" y moverlos al punto (0,0)
    elemento.set_color_hex("#808080")
    elemento.mover_a(punto_origen)
    
    # AHORA SÍ FUNCIONA: Sumamos el área de cada elemento
    area_total += elemento.calcularArea() 
    
    # Imprimimos para ver cómo quedó cada figura
    print(elemento)

# 5. Imprimir el área total final
print("\n" + "="*40)
print(f"Área total ocupada por los elementos: {area_total:.2f} px")
print("="*40)