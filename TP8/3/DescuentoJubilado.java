public class DescuentoJubilado implements Descuento {
    @Override
    public double calcularMontoDescontado(double montoBase) {
        return montoBase * 0.15; // 15% de descuento
    }
}