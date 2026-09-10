import java.util.ArrayList;
import java.util.List;

public class Factura {
    private String tipoComprobante;
    private List<LineaFactura> lineas;
    private List<Descuento> estrategiasDeDescuento;

    public Factura(String tipoComprobante, List<LineaFactura> lineas) {
        this.tipoComprobante = tipoComprobante;
        this.lineas = lineas;
        this.estrategiasDeDescuento = new ArrayList<>();
    }

    public void agregarPromocion(Descuento descuento) {
        this.estrategiasDeDescuento.add(descuento);
    }

    public double calcularTotal() {
        double subtotal = 0;
        
        for(LineaFactura linea : lineas) {
            subtotal += linea.calcularSubtotal(); 
        }

        double totalFinal = subtotal;
        for(Descuento desc : estrategiasDeDescuento) {
            totalFinal = totalFinal - desc.calcularMontoDescontado(totalFinal);
        }

        return totalFinal;
    }
}
