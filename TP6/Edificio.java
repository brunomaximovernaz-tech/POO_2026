public class Edificio implements ImpactoEcologico {
    private static final double FACTOR_CO2_GAS = 1.93;

    private String nombre;
    private double metrosCuadrados;
    private double consumoGasMensual;

    public Edificio(String nombre, double metrosCuadrados, double consumoGasMensual) {
        this.nombre = nombre;
        this.metrosCuadrados = metrosCuadrados;
        this.consumoGasMensual = consumoGasMensual;
    } // Corregido: Faltaba esta llave de cierre

    public double calcularCostoEnergiaPorM2(double tarifaporM3) {
        return (consumoGasMensual * tarifaporM3) / metrosCuadrados;
    } // Corregido: Faltaba esta llave de cierre

    public String getNombre() {
        return nombre;
    }

    public double getMetrosCuadrados() {
        return metrosCuadrados;
    }

    @Override
    public double obtenerImpactoEcologico() { // Corregido: Sobraba un espacio entre "obtener" e "ImpactoEcologico"
        return consumoGasMensual * FACTOR_CO2_GAS;
    } // Corregido: Faltaba esta llave de cierre

    @Override
    public String identificar() { // Corregido: Se cambió "Identificar" a "identificar" con minúscula inicial para coincidir con la interfaz
        // Corregido: Se reemplazaron las dos comillas simples ('') por una comilla doble (") al inicio del texto
        return "Edificio [" + nombre + ", " + metrosCuadrados + " m2]"; 
    }
}