

public class LineaFactura {
    private int cantidad;
    private Producto producto;
    
    // Resguardo histórico (Punto 1)
    private double precioUnitarioFacturado;
    private double porcentajeIvaFacturado;

    public LineaFactura(int cantidad, Producto producto) {
        this.cantidad = cantidad;
        this.producto = producto;
        // Congelamos el estado al momento de la venta
        this.precioUnitarioFacturado = producto.getPrecioBase();
        this.porcentajeIvaFacturado = producto.getPorcentajeIva();
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

    // --- CÁLCULOS INTERNOS: EXPERTO EN INFORMACIÓN (Soluciona Punto 2) ---

    public double subtotalBruto() {
        return redondear(this.cantidad * this.precioUnitarioFacturado);
    }

    public double calcularDescuento(double porcentajeDescuentoGlobal) {
        // Se aplica el descuento sobre el bruto antes de impuestos (Punto 5 - ARCA)
        return redondear(subtotalBruto() * (porcentajeDescuentoGlobal / 100.0));
    }

    public double subtotalNeto(double porcentajeDescuentoGlobal) {
        return redondear(subtotalBruto() - calcularDescuento(porcentajeDescuentoGlobal));
    }

    public double calcularIva(double porcentajeDescuentoGlobal) {
        return redondear(subtotalNeto(porcentajeDescuentoGlobal) * (porcentajeIvaFacturado / 100.0));
    }

    public double totalConIva(double porcentajeDescuentoGlobal) {
        return redondear(subtotalNeto(porcentajeDescuentoGlobal) + calcularIva(porcentajeDescuentoGlobal));
    }

    private double redondear(double valor) {
        return Math.round(valor * 100.0) / 100.0;
    }
}