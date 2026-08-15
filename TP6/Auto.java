public class Auto implements ImpactoEcologico {
    // Mantenemos la constante original
    private static final double FACTOR_CO2_GAS = 2.31;

    String modelo;
    double kilometrosRecorridos;
    double rendimientoKmPorLitro;

    public Auto(String modelo, double kilometrosRecorridos, double rendimientoKmPorLitro) {
        this.modelo = modelo;
        this.kilometrosRecorridos = kilometrosRecorridos;
        this.rendimientoKmPorLitro = rendimientoKmPorLitro;
    }

    public double calcularLitrosConsumidos() {
        return kilometrosRecorridos / rendimientoKmPorLitro;
    }

    public String getModelo() {
        return modelo;
    }

    public double getKilometrosRecorridos() {
        return kilometrosRecorridos;
    }

    @Override
    public double obtenerImpactoEcologico() {
        // Corregido: Ahora multiplicamos usando la constante FACTOR_CO2_GAS
        return calcularLitrosConsumidos() * FACTOR_CO2_GAS;
    }

    @Override
    public String identificar() {
        return "Auto [" + modelo + ", " + getKilometrosRecorridos() + " km]";
    }
}