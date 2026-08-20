import sqlite3

# 1. Clase encargada únicamente de la Lógica de Negocio
class Factura:
    def __init__(self, nombre_cliente, monto_base, tipo_cliente):
        self.nombre_cliente = nombre_cliente
        self.monto_base = monto_base
        self.tipo_cliente = tipo_cliente
        self.total_final = self.calcular_total()

    def calcular_total(self):
        descuento = 0.0
        if self.tipo_cliente == "VIP":
            descuento = self.monto_base * 0.20
        elif self.tipo_cliente == "REGULAR":
            descuento = self.monto_base * 0.10
        return self.monto_base - descuento

# 2. Clase encargada únicamente de la Persistencia (Base de Datos)
class FacturaRepositorio:
    def guardar(self, factura):
        try:
            conexion = sqlite3.connect("mi_empresa.db")
            cursor = conexion.cursor()
            query = f"INSERT INTO facturas (cliente, total) VALUES ('{factura.nombre_cliente}', {factura.total_final})"
            cursor.execute(query)
            conexion.commit()
            conexion.close()
        except Exception as e:
            print(f"Error bd: {e}")

# 3. Clase encargada únicamente de la Interfaz / Presentación
class FacturaImpresora:
    def imprimir(self, factura):
        print(f"FACTURA: {factura.nombre_cliente} | Total: ${factura.total_final}")

# Ejemplo de uso:
# mi_factura = Factura("Empresa S.A.", 1000.0, "VIP")
# impresora = FacturaImpresora()
# impresora.imprimir(mi_factura)
# repositorio = FacturaRepositorio()
# repositorio.guardar(mi_factura)