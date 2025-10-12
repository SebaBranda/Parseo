Traza del Analizador ASDP LL(1)
--- INICIO DEL PARSEO LL(1) ---
PILA                             | ENTRADA (Lookahead)  | ACCION
----------------------------------------------------------------------
$S                               | INICIO               | EXPANDIR S -> INICIO I FIN
$FIN I INICIO                    | INICIO               | MATCH INICIO
$FIN I                           | MOVER                | EXPANDIR I -> INSTRUCCION I
$FIN I INSTRUCCION               | MOVER                | EXPANDIR INSTRUCCION -> MOVER
$FIN I MOVER                     | MOVER                | EXPANDIR MOVER -> MOVER DIRECCION
$FIN I DIRECCION MOVER           | MOVER                | MATCH MOVER
$FIN I DIRECCION                 | NORTE                | EXPANDIR DIRECCION -> NORTE
$FIN I NORTE                     | NORTE                | MATCH NORTE
$FIN I                           | FIN                  | EXPANDIR I -> epsilon
$FIN                             | FIN                  | MATCH FIN
$                                | $                    | ÉXITO: Cadena aceptada.
----------------------------------------------------------------------
RESULTADO FINAL: ÉXITO: Cadena aceptada.

## Conjuntos PRIM (FIRST) y SIG (FOLLOW)

| **Conjunto** | **Cálculo**                      | **Resultado**               |
| :----------- | :------------------------------- | :-------------------------- |
| **PRIM(C)**  | FIRST(C → SINO I) ∪ FIRST(C → ϵ) | { SINO, ϵ }                 |
| **SIG(C)**   | FOLLOW(C)                        | { FIN, MOVER, SI, SINO, … } |

## Conjuntos Predictivos (PRED)

| **Producción** | **PRED(C → α)** | **Resultado**               |
| :------------- | :-------------- | :-------------------------- |
| **C → SINO I** | FIRST(SINO I)   | { SINO }                    |
| **C → ϵ**      | FOLLOW(C)       | { FIN, MOVER, SI, SINO, … } |

## Test de Condición LL(1)

| **Condición**                  | **Operación**                          | **Intersección** | **¿Es LL(1)?**                           |
| :----------------------------- | :------------------------------------- | :--------------- | :--------------------------------------- |
| PRED(C → SINO I) ∩ PRED(C → ϵ) | { SINO } ∩ { FIN, MOVER, SI, SINO, … } | { SINO }         | ❌ No, porque la intersección no es vacía |

