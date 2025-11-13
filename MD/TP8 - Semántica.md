## Semántica "Caminante"

Este cuadro indica el tipo resultado de aplicar cada operador a operandos de tipos dados. — = operación inválida.

A) Operadores relacionales (comparadores) — resultado BOOL si los operandos son compatibles

| Operador \ (Tipo left, Tipo right) |   INT  |  BOOL  |                   DIR                  |   STR  |
| ---------------------------------: | :----: | :----: | :------------------------------------: | :----: |
|     `ES_MAYOR_QUE`, `ES_MENOR_QUE` | `BOOL` |   `—`  |                   `—`                  |   `—`  |
|                `IGUAL`, `DISTINTO` | `BOOL` | `BOOL` | `BOOL` (solo igualdad con mismas dirs) | `BOOL` |

Reglas:

- Comparaciones numéricas (ES_MAYOR_QUE, ES_MENOR_QUE) válidas solo con INT.

- IGUAL/DISTINTO válidos entre mismos tipos (INT-INT, BOOL-BOOL, DIR-DIR, STR-STR).

- No se permite comparar DIR con INT (salvo conversión explícita que no existe en Caminante).

### B) Asignación / paso de parámetro (compatibilidad)

| Destino \ Origen | INT | BOOL | DIR | STR |
| ---------------: | :-: | :--: | :-: | :-: |
|              INT |  OK |  ERR | ERR | ERR |
|             BOOL | ERR |  OK  | ERR | ERR |
|              DIR | ERR |  ERR |  OK | ERR |
|              STR | ERR |  ERR | ERR |  OK |

2) Cuadro semántico — Secuencia 1

Secuencia: inicio mover norte fin

### 2.1. Datos previos (TT / TS relevantes)

## TT (fragmento):

- DIR — tipo enumerado {NORTE, SUR, ESTE, OESTE}.

- ACT — tipo de acciones (void / no produce valor).

TS (fragmento):

- mover : action signature mover(DIR) : ACT

- NORTE : literal de tipo DIR

- inicio / fin : palabras clave de estructura (no variables)

## 2.2. Cuadro de comprobaciones (paso a paso)

| Paso | Nodo / Sentencia    | Acción semántica                                               | Consultas TT/TS                           |        Resultado       |
| :--: | :------------------ | :------------------------------------------------------------- | :---------------------------------------- | :--------------------: |
|   1  | `inicio`            | Abrir ámbito global / iniciar programa                         | —                                         |  OK (inicia análisis)  |
|   2  | `mover`             | Reconocer llamada a acción                                     | Buscar `mover` en TS → firma `mover(DIR)` |           OK           |
|   3  | argumento `norte`   | Tipo del argumento                                             | Buscar `NORTE` en TS → tipo `DIR`         |           OK           |
|   4  | verificación firma  | Comprobar compatibilidad `DIR` → parámetro `DIR`               | Cubo de asignación: `DIR` ← `DIR` = OK    |           OK           |
|   5  | ejecución semántica | (no hay efectos semanticamente relevantes aquí, solo chequeos) | —                                         |           OK           |
|   6  | `fin`               | Cerrar ámbito y verificar que todo fue consistente             | —                                         | OK — programa aceptado |

Observación final: No hay errores; todas las comprobaciones pasan.

---

### 3) Cuadro semántico — Secuencia 2

Secuencia:

```
inicio
mover norte
si obstaculo entonces mover este
fin
```

## 3.1. Datos previos (TT / TS relevantes)

TT:

- DIR, BOOL, ACT (como antes).

TS:

- mover(DIR) : acción.

- NORTE, ESTE : DIR.

- obstaculo : símbolo de condición — en este ejemplo lo tratamos como identificador con tipo BOOL (debe existir en TS; si no, semántica marca error de identificador no declarado).

- si, entonces : palabras clave de control.

Nota: si 'obstaculo' fuera una variable/identificador, debió ser declarada antes; en nuestros ejemplos la damos por presente en TS como obstaculo: BOOL.

## 3.2. Cuadro de comprobaciones (paso a paso)

| Paso | Nodo / Sentencia                                 | Acción semántica                          | Consultas TT/TS                                            |                            Resultado                           |
| :--: | :----------------------------------------------- | :---------------------------------------- | :--------------------------------------------------------- | :------------------------------------------------------------: |
|   1  | `inicio`                                         | Abrir ámbito global                       | —                                                          |                               OK                               |
|   2  | `mover norte`                                    | `mover` lookup                            | TS: `mover(DIR)` → OK                                      |                               OK                               |
|   3  | arg `norte`                                      | Tipo `DIR`                                | TS: `NORTE` → `DIR`                                        |                               OK                               |
|   4  | comprobar firma                                  | `DIR` vs `DIR` → OK                       | Cubo asignación: OK                                        |                               OK                               |
|   5  | `si obstaculo entonces ...` — analizar condición | Buscar `obstaculo` en TS: **existe?**     | Si existe → obtener tipo; si no → **ERR: id no declarado** |                                                                |
|   6  | tipo de `obstaculo`                              | Debe ser `BOOL`                           | TT/TS: `obstaculo.type == BOOL` ?                          | Si `BOOL` → OK ; si != `BOOL` → **ERR: condición no booleana** |
|   7  | bloque `entonces` interno `mover este`           | Igual comprobación que en 2–4 para `este` | TS: `ESTE` → `DIR`; `mover(DIR)` → OK                      |                               OK                               |
|   8  | `fin`                                            | Cerrar ámbito                             | —                                                          |           OK — programa aceptado (si no hubo errores)          |

---
