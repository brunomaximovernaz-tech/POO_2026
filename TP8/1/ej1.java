public class LineaFactura {
    private int cantidad;
    private Producto producto; 
    
    // Nuevos atributos para resolver el problema del tiempo y guardar el dato histórico[cite: 3]
    private double precioUnitarioFacturado; 
    private double porcentajeIvaFacturado;

    public LineaFactura(int cantidad, Producto producto) {
        this.cantidad = cantidad;
        this.producto = producto;
        
        // Se congelan los valores exactos en el momento en que se instancia la línea[cite: 3]
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
}