import java.util.ArrayList;
import java.util.List;

public class EmpleadoService {
    private static List<Empleado> empleados = new ArrayList<>();
    private static int proximoLegajo = 1;

    // Se propaga la EnteroPositivoException que lanza el setLegajo
    public static Boolean agregar(Empleado empleado) throws EnteroPositivoException {
        empleado.setLegajo(proximoLegajo++);
        return empleados.add(empleado);
    }

    public static Empleado mayorSueldo() throws CollectionVaciaException {
        if (empleados.isEmpty()) {
            throw new CollectionVaciaException("No hay empleados.");
        }
        
        Empleado max = empleados.get(0);
        for (Empleado e : empleados) {
            if (e.getSueldo() > max.getSueldo()) {
                max = e;
            }
        }
        return max;
    }

    public static Double sueldoPromedio() throws CollectionVaciaException {
        if (empleados.isEmpty()) {
            throw new CollectionVaciaException("No hay empleados.");
        }
        
        double suma = 0;
        for (Empleado e : empleados) {
            suma += e.getSueldo();
        }
        return suma / empleados.size();
    }

    // Busca y elimina por nombre como indica el código base del PDF
    public static void eliminar(String nombre) throws CollectionVaciaException, NoEncontradoException {
        if (empleados.isEmpty()) {
            throw new CollectionVaciaException("No hay empleados.");
        }

        boolean eliminado = empleados.removeIf(e -> e.getNombre().equals(nombre));
        
        if (!eliminado) {
            throw new NoEncontradoException("No se encontro el empleado.");
        }
    }
}