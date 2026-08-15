import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Corregido: Se eliminaron los indicadores 'nombre:', 'metrosCuadrados:', y 'consumoGasMensual:'
        Edificio edificio = new Edificio("Torre Central", 500.0, 300.0);
        
        // Corregido: Se eliminaron los indicadores 'modelo:', 'kilometrosRecorridos:' y 'rendimientoKmPo...'
        Auto auto = new Auto("Toyota Corolla", 1200.0, 14.0);
        
        // Corregido: Se eliminaron los indicadores 'tipo:' y 'kilometrosRecorridos:'
        Bicicleta bicicleta = new Bicicleta("Montaña", 150.0);

        ArrayList<ImpactoEcologico> lista = new ArrayList<>();
        lista.add(edificio);
        lista.add(auto);
        lista.add(bicicleta);

        for (ImpactoEcologico item : lista) {
            // Corregido: Se eliminó el indicador 'format:'
            System.out.printf("%s -> Impacto ecologico: %.2f kg de CO2%n",
                    item.identificar(), item.obtenerImpactoEcologico());
        }
    }
}