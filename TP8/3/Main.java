import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // 1. Creamos un producto y una línea
        Producto tele = new Producto("Televisor", 60000.0, 0.21);
        LineaFactura linea1 = new LineaFactura(1, tele);
        
        List<LineaFactura> misLineas = new ArrayList<>();
        misLineas.add(linea1);

        // 2. Creamos la factura
        Factura miFactura = new Factura("Ticket B", misLineas);

        // 3. Le inyectamos los descuentos dinámicamente
        miFactura.agregarPromocion(new DescuentoPorVolumen());
        miFactura.agregarPromocion(new DescuentoJubilado());

        // 4. Calculamos e imprimimos
        System.out.println("El total a pagar es: $" + miFactura.calcularTotal());
    }
}