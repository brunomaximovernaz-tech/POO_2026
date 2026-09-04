

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Factura {
    private String tipoComprobante; // "A" o "B"
    private double porcentajeDescuento; // Ej: 15.0
    private List<LineaFactura> lineas;

    public Factura(String tipoComprobante, double porcentajeDescuento) {
        this.tipoComprobante = tipoComprobante;
        this.porcentajeDescuento = porcentajeDescuento;
        this.lineas = new ArrayList<>();
    }

    public void agregarLinea(Producto producto, int cantidad) {
        this.lineas.add(new LineaFactura(cantidad, producto));
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

    // Cumple con la Ley de Demeter: le pide a la línea sus subtotales en lugar de calcularlos afuera
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
        return redondear(calcularTotalNeto() + calcularTotalIva());
    }

    // Desglose impositivo exigido por ARCA
    public Map<Double, double[]> obtenerDesgloseImpuestos() {
        Map<Double, double[]> desglose = new LinkedHashMap<>();

        for (LineaFactura linea : lineas) {
            double tasa = linea.getPorcentajeIvaFacturado();
            double neto = linea.subtotalNeto(this.porcentajeDescuento);
            double iva = linea.calcularIva(this.porcentajeDescuento);

            if (!desglose.containsKey(tasa)) {
                desglose.put(tasa, new double[]{0.0, 0.0});
            }

            double[] acumuladores = desglose.get(tasa);
            acumuladores[0] = redondear(acumuladores[0] + neto);
            acumuladores[1] = redondear(acumuladores[1] + iva);
        }

        return desglose;
    }

    private double redondear(double valor) {
        return Math.round(valor * 100.0) / 100.0;
    }
}