# TP 9 - GRASP y SOLID aplicados: Sistema SmartTicket

**Materia:** Programación Orientada a Objetos
**Implementación:** Parte 2 - Historia de Usuario 1 (Selección y Cotización)

## Justificación Arquitectónica

### Principio de Responsabilidad Única (SRP - SOLID)

Se separaron las responsabilidades dividiendo el flujo en capas para evitar el código espagueti. El controlador (`routers.py`) tiene ahora una única razón para cambiar: modificaciones en el protocolo HTTP. Su única tarea es recibir la petición, delegar el procesamiento y devolver la respuesta HTTP. Toda la lógica condicional y los cálculos matemáticos exigidos por los escenarios de la Historia de Usuario fueron extraídos y encapsulados en la capa de servicio (`services.py`).

### Experto en Información (GRASP)

Para la validación de disponibilidad física y el cálculo del subtotal, se delegó la responsabilidad a la clase `CotizacionService`. Esta clase actúa como la experta en información porque, al recibir el payload de la petición y la sesión de la base de datos, posee todos los datos necesarios para contabilizar las instancias de `Entrada` en estado "Disponible" y ejecutar las multiplicaciones, sin que el controlador deba conocer estas reglas del dominio.

### Inyección de Dependencias

Se respeta el desacoplamiento inyectando la sesión del repositorio (`Session`) directamente en el constructor del servicio (`CotizacionService(db)`) desde el endpoint en FastAPI mediante `Depends(get_db)`. Esto garantiza que la lógica de validación no instancie sus propias conexiones rígidamente, permitiendo aislar la clase para realizar futuras pruebas.