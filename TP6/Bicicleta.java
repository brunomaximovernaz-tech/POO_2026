public class Bicicleta implements ImpactoEcologico {

    String tipo;
    double kilometrosRecorridos;

    double factorCo2Gasolina = 2.31;
    double rendimientoAutoReferencia = 10.0;

    public Bicicleta(String tipo, double kilometrosRecorridos) {
        this.tipo = tipo;
        this.kilometrosRecorridos = kilometrosRecorridos;
    }

    public double calcularCaloriasQuemadas() {
        return kilometrosRecorridos * 30;
    }
public String getTipo() {
    return tipo;
}

public double getKilometrosRecorridos() {
    return kilometrosRecorridos;
}

public double obtenerImpactoEcologico() {
    double litrosEquivalentes = kilometrosRecorridos / rendimientoAutoReferencia;
    return litrosEquivalentes * factorCo2Gasolina * -1;
}

@Override
public String identificar() {
    return "Bicicleta [" + tipo + ", " + kilometrosRecorridos + " km]";
}
}