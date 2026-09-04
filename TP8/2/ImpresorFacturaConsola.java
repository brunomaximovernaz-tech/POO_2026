

import java.util.Map;

/**
 * Clase artificial encargada únicamente de imprimir la factura por pantalla.
 * Separa la vista/presentación de las clases del modelo de dominio (Punto 4).
 */
public class ImpresorFacturaConsola {

    public static void imprimir(Factura factura) {
        System.out.println("==================================================");
        System.out.println("             SUPERMERCADO LA GRAN PROVISIÓN       ");
        System.out.println("==================================================");
        System.out.printf("COMPROBANTE TIPO %s | Descuento Aplicado: %.1f%%%n", 
                factura.getTipoComprobante(), factura.getPorcentajeDescuento());
        System.out.println("--------------------------------------------------");
        System.out.printf("%-5s | %-15s | %-8s | %-10s%n", 
                "Cant.", "Producto", "P.Unit", "Neto c/Desc");
        System.out.println("--------------------------------------------------");

        for (LineaFactura linea : factura.getLineas()) {
            System.out.printf("%-5d | %-15s | %-8.2f | %-10.2f%n", 
                    linea.getCantidad(),
                    linea.getProducto().getNombre(),
                    linea.getPrecioUnitarioFacturado(),
                    linea.subtotalNeto(factura.getPorcentajeDescuento()));
        }

        System.out.println("--------------------------------------------------");
        System.out.println("Desglose Impositivo por Alícuota (Exigido por ARCA):");
        Map<Double, double[]> desglose = factura.obtenerDesgloseImpuestos();
        for (Map.Entry<Double, double[]> entrada : desglose.entrySet()) {
            double tasa = entrada.getKey();
            double neto = entrada.getValue()[0];
            double iva = entrada.getValue()[1];
            System.out.printf("  Tasa IVA %5.1f%% | Neto Imponible: $%8.2f | Monto IVA: $%8.2f%n", 
                    tasa, neto, iva);
        }
        System.out.println("--------------------------------------------------");

        System.out.printf("TOTAL NETO FACTURADO:    $%8.2f%n", factura.calcularTotalNeto());
        System.out.printf("TOTAL IVA FACTURADO:     $%8.2f%n", factura.calcularTotalIva());
        System.out.printf("TOTAL GENERAL FACTURADO: $%8.2f%n", factura.calcularTotalGeneral());
        System.out.println("==================================================");
        System.out.println();
    }
}