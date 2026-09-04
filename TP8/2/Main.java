

public class Main {
    public static void main(String[] args) {
        // 1. Instanciar productos del catálogo
        Producto limpieza = new Producto("Limpieza", 5000.0, 21.0);
        Producto carnes = new Producto("Carnes", 4000.0, 10.5);
        Producto leche = new Producto("Leche", 1000.0, 0.0);

        // 2. Crear una Factura B con 15% de descuento
        Factura facturaB = new Factura("B", 15.0);
        
        facturaB.agregarLinea(limpieza, 1);
        facturaB.agregarLinea(carnes, 1);
        facturaB.agregarLinea(leche, 1);

        // 3. Imprimir factura
        ImpresorFacturaConsola.imprimir(facturaB);
    }
}
