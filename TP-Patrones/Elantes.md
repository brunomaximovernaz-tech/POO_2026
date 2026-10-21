```mermaid
classDiagram
    class SistemaBolsaXML {
        +descargarDatos()
        +procesarPrediccion()
    }
    
    class BibliotecaPrediccionJSON {
        +analizarMercado(datosJSON)
    }

    SistemaBolsaXML ..> BibliotecaPrediccionJSON : Error por incompatibilidad de datos
    
    note for SistemaBolsaXML "El sistema base usa XML\ny no puede conectarse a\nla biblioteca que exige JSON."
```