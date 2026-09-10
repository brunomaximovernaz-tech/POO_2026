public class DescuentoPorVolumen implements Descuento {
    @Override
    public double calcularMontoDescontado(double montoBase) {
        if (montoBase > 50000) {
            return montoBase * 0.10; // 10% si supera los $50.000
        }
        return 0; 
    }
}
}
