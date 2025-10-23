Entrada: INICIO MOVER NORTE FIN $

| Paso | Pila                     | Entrada                    | Acción                                                                       |
| :--: | :----------------------- | :------------------------- | :--------------------------------------------------------------------------- |
|   1  | —                        | `INICIO MOVER NORTE FIN $` | **Shift** `INICIO`                                                           |
|   2  | INICIO                   | `MOVER NORTE FIN $`        | **Shift** `MOVER`                                                            |
|   3  | INICIO MOVER             | `NORTE FIN $`              | **Shift** `NORTE`                                                            |
|   4  | INICIO MOVER NORTE       | `FIN $`                    | **Reduce** `NORTE → <direccion>`                                             |
|   5  | INICIO MOVER <direccion> | `FIN $`                    | **Reduce** `MOVER <direccion> → <movimiento>`                                |
|   6  | INICIO <movimiento>      | `FIN $`                    | **Reduce** `<movimiento> → <instruccion>`                                    |
|   7  | INICIO <instruccion>     | `FIN $`                    | **Reduce** `<instruccion> → <bloque>` (asumiendo <bloque> → <instruccion> ε) |
|   8  | INICIO <bloque>          | `FIN $`                    | **Shift** `FIN`                                                              |
|   9  | INICIO <bloque> FIN      | `$`                        | **Reduce** `INICIO <bloque> FIN → <programa>`                                |
|  10  | `<programa>`             | `$`                        | **Accept**                                                                   |

Resultado: la cadena es aceptada también por el análisis ascendente, con las mismas reducciones esperadas.
