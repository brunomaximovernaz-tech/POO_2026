import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.LinkedHashMap;

class Producto {
    private String nombre;
    private double precioBase;
    private double porcentajeIva;

    public Producto(String nombre, double precioBase, double porcentajeIva) {
        this.nombre = nombre;
        this.precioBase = precioBase;
        this.porcentajeIva = porcentajeIva;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecioBase() {
        return precioBase;
    }

    public double getPorcentajeIva() {
        return porcentajeIva;
    }
}

class LineaFactura {
    private int cantidad;
    private Producto producto;
    // Congelamiento histórico (Punto 1)
    private double precioUnitarioFacturado;
    private double porcentajeIvaFacturado;

    public LineaFactura(int cantidad, Producto producto) {
        this.cantidad = cantidad;
        this.producto = producto;
        this.precioUnitarioFacturado = producto.getPrecioBase();
        this.porcentajeIvaFacturado = producto.getPorcentajeIva();
    }

    private double redondear(double valor) {
        return Math.round(valor * 100.0) / 100.0;
    }

    public int getCantidad() {
        return cantidad;
    }

    public Producto getProducto() {
        return producto;
    }

    public double getPrecioUnitarioFacturado() {
        return precioUnitarioFacturado;
    }

    public double getPorcentajeIvaFacturado() {
        return porcentajeIvaFacturado;
    }

    public double subtotalBruto() {
        return redondear(this.cantidad * this.precioUnitarioFacturado);
    }

    public double calcularDescuento(double porcentajeDescuentoGlobal) {
        // El descuento se aplica sobre el bruto de la línea antes de impuestos
        return redondear(this.subtotalBruto() * (porcentajeDescuentoGlobal / 100.0));
    }

    public double subtotalNeto(double porcentajeDescuentoGlobal) {
        return redondear(this.subtotalBruto() - this.calcularDescuento(porcentajeDescuentoGlobal));
    }

    public double calcularIva(double porcentajeDescuentoGlobal) {
        return redondear(this.subtotalNeto(porcentajeDescuentoGlobal) * (this.porcentajeIvaFacturado / 100.0));
    }

    public double totalConIva(double porcentajeDescuentoGlobal) {
        return redondear(this.subtotalNeto(porcentajeDescuentoGlobal) + this.calcularIva(porcentajeDescuentoGlobal));
    }
}

class Factura {
    private String tipoComprobante; // "A" o "B"
    private double porcentajeDescuento; // Ej: 15.0 para 15%
    private List<LineaFactura> lineas;

    public Factura(String tipoComprobante, double porcentajeDescuento, List<LineaFactura> lineas) {
        this.tipoComprobante = tipoComprobante;
        this.porcentajeDescuento = porcentajeDescuento;
        this.lineas = lineas;
    }

    public String getTipoComprobante() {
        return tipoComprobante;
    }

    public double getPorcentajeDescuento() {
        return porcentajeDescuento;
    }

    public List<LineaFactura> getLineas() {
        return lineas;
    }

    private double redondear(double valor) {
        return Math.round(valor * 100.0) / 100.0;
    }

    // Agrupar neto e IVA por alícuota
    public Map<Double, Map<String, Double>> obtenerResumenImpuestos() {
        Map<Double, Map<String, Double>> resumen = new LinkedHashMap<>();
        for (LineaFactura linea : lineas) {
            double ivaRate = linea.getPorcentajeIvaFacturado();
            double neto = linea.subtotalNeto(this.porcentajeDescuento);
            double iva = linea.calcularIva(this.porcentajeDescuento);

            if (!resumen.containsKey(ivaRate)) {
                Map<String, Double> valores = new LinkedHashMap<>();
                valores.put("neto", 0.0);
                valores.put("iva", 0.0);
                resumen.put(ivaRate, valores);
            }

            Map<String, Double> valoresActuales = resumen.get(ivaRate);
            valoresActuales.put("neto", redondear(valoresActuales.get("neto") + neto));
            valoresActuales.put("iva", redondear(valoresActuales.get("iva") + iva));
        }
        return resumen;
    }

    public double calcularTotalNeto() {
        double total = 0.0;
        for (LineaFactura linea : lineas) {
            total += linea.subtotalNeto(this.porcentajeDescuento);
        }
        return redondear(total);
    }

    public double calcularTotalIva() {
        double total = 0.0;
        for (LineaFactura linea : lineas) {
            total += linea.calcularIva(this.porcentajeDescuento);
        }
        return redondear(total);
    }

    public double calcularTotalGeneral() {
        return redondear(this.calcularTotalNeto() + this.calcularTotalIva());
    }
}

// Fabricación Pura (Pure Fabrication) para separar la visualización de la lógica
class ImpresorFacturaConsola {
    public static void imprimir(Factura factura) {
        System.out.println("==================================================");
        System.out.println("             FACTURA TIPO " + factura.getTipoComprobante() + "             ");
        System.out.println("==================================================");
        System.out.printf("%-5s | %-15s | %-8s | %-11s%n", "Cant.", "Detalle", "P.Unit", "Neto c/Desc");
        System.out.println("--------------------------------------------------");
        for (LineaFactura linea : factura.getLineas()) {
            double netoDesc = linea.subtotalNeto(factura.getPorcentajeDescuento());
            System.out.printf("%-5d | %-15s | %-8.2f | %-11.2f%n", 
                linea.getCantidad(), 
                linea.getProducto().getNombre(), 
                linea.getPrecioUnitarioFacturado(), 
                netoDesc
            );
        }
        System.out.println("--------------------------------------------------");

        Map<Double, Map<String, Double>> resumenIva = factura.obtenerResumenImpuestos();

        System.out.println("Desglose Impositivo por Alícuota (ARCA):");
        for (Map.Entry<Double, Map<String, Double>> entrada : resumenIva.entrySet()) {
            double tasa = entrada.getKey();
            Map<String, Double> valores = entrada.getValue();
            System.out.printf("  Tasa IVA %4.1f%% | Neto: $%8.2f | IVA: $%8.2f%n", 
                tasa, 
                valores.get("neto"), 
                valores.get("iva")
            );
        }
        System.out.println("--------------------------------------------------");

        System.out.printf("Total Neto Facturado: $%1.2f%n", factura.calcularTotalNeto());
        System.out.printf("Total IVA Facturado:  $%1.2f%n", factura.calcularTotalIva());
        System.out.printf("TOTAL GENERAL:        $%1.2f%n", factura.calcularTotalGeneral());
        System.out.println("==================================================");
    }
}

public class SistemaFacturacion {
    public static void main(String[] args) {
        // Probar la matemática del problema ARCA
        // 1 Factura original de $10,000 bruto con 15% de descuento
        Producto prod1 = new Producto("Limpieza (21%)", 5000.0, 21.0);
        Producto prod2 = new Producto("Carnes (10.5%)", 4000.0, 10.5);
        Producto prod3 = new Producto("Leche (Exento)", 1000.0, 0.0);

        List<LineaFactura> lineas = new ArrayList<>();
        lineas.add(new LineaFactura(1, prod1));
        lineas.add(new LineaFactura(1, prod2));
        lineas.add(new LineaFactura(1, prod3));

        Factura facturaB = new Factura("B", 15.0, lineas);
        ImpresorFacturaConsola.imprimir(facturaB);
    }
}
