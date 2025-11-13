# TT y TS


# TT — Tabla de Tipos "Caminante"

---

| Cod | Nombre            | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito | Observaciones |
| --- | ----------------- | -------- | ----- | --------- | ------ | ------ | ------ | ------------- |
| 0   | accion            | -1       | -1    | 1         | -1     | -1     | 0      | tipo base para acciones/verbos del lenguaje (mover, manifestar, ...)
| 1   | direccion         | -1       | -1    | 1         | 0      | 3      | 0      | enumerado: {norte=0, sur=1, este=2, oeste=3}
| 2   | condicion         | -1       | -1    | 1         | -1     | -1     | 0      | tipo lógico (booleano) usado en condicionales y bucles
| 3   | instruccion       | 0        | -1    | 1         | -1     | -1     | 0      | acción o estructura de control (movimiento, accion, condicional, bucle, declaracion)
| 4   | programa          | 3        | -1    | *         | -1     | -1     | 0      | secuencia de `instruccion`
| 5   | num               | -1       | -1    | 1         | -inf   | +inf   | 0      | número entero o real (NUM token)
| 6   | cadena            | -1       | -1    | 1         | -      | -      | 0      | valor literal de cadena (CADENA token)
| 7   | identificador     | -1       | -1    | 1         | -      | -      | 0      | referencia a variable (IDENT token)
| 8   | bloque            | 4        | -1    | *         | -      | -      | 0      | secuencia de instrucciones con ámbito propio
| 9   | repeticion_count  | 5        | -1    | 1         | 0      | +inf   | 0      | número de repeticiones (NUM)


---

## Tabla de Símbolos (símbolos reservados, acciones y literales comunes)

La tabla siguiente documenta las palabras reservadas, acciones y literales que el parser
trata como símbolos con su categoría y tipos esperados.

| Cod | Nombre             | Categoría       | Tipo (Code) | NumPar | ListaPar (tipos)         | Ámbito | Observaciones |
| --- | ------------------ | --------------- | ----------- | ------ | ------------------------ | ------ | ------------- |
| 0   | inicio             | palabra_clave   | —           | -1     | null                     | 0      | marca inicio de programa
| 1   | fin                | palabra_clave   | —           | -1     | null                     | 0      | marca fin de programa
| 2   | mover              | acción          | 0 (accion)  | 1      | [1] (direccion)          | 0      | firma: mover(direccion)
| 3   | manifestar         | acción          | 0 (accion)  | 1      | [6] (cadena)             | 0      | firma: manifestar(cadena)
| 4   | interactuar_con    | acción          | 0 (accion)  | 1      | [7] (identificador)      | 0      | firma aproximada; depende de semántica
| 5   | transicionar_a     | acción          | 0 (accion)  | 1      | [7] (identificador)      | 0      | cambiar estado/ubicación
| 6   | si                 | palabra_clave   | —           | -1     | null                     | 0      | estructura condicional
| 7   | entonces           | palabra_clave   | —           | -1     | null                     | 0      | separador condicional
| 8   | sino               | palabra_clave   | —           | -1     | null                     | 0      | rama alterna condicional
| 9   | repetit            | palabra_clave   | —           | -1     | null                     | 0      | inicio bucle repetir (alias en docs)
| 10  | mientras           | palabra_clave   | —           | -1     | null                     | 0      | inicio bucle mientras
| 11  | establecer (establece) | acción      | —           | 2      | [7, valor]               | 0      | establece IDENT A valor (asignación)
| 12  | norte              | literal         | 1 (direccion) | -1   | null                     | 0      | constante de tipo dirección
| 13  | sur                | literal         | 1 (direccion) | -1   | null                     | 0      | constante de tipo dirección
| 14  | este               | literal         | 1 (direccion) | -1   | null                     | 0      | constante de tipo dirección
| 15  | oeste              | literal         | 1 (direccion) | -1   | null                     | 0      | constante de tipo dirección
| 16  | NUM                | token literal   | 5 (num)     | -1     | null                     | 0      | token numérico
| 17  | CADENA             | token literal   | 6 (cadena)  | -1     | null                     | 0      | token cadena
| 18  | IDENT              | token id        | 7 (identificador) | -1| null                     | 0      | token identificador

Notas:
- `NumPar` indica el número de parámetros que la acción espera.
- `ListaPar` lista el tipo esperado de cada parámetro.

---

## Secuencia 1:
```
inicio mover norte fin
```


## Tabla de Tipos

| Línea PRG | Cod | Nombre      | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito | Observaciones                      |
| --------- | --- | ----------- | -------- | ----- | --------- | ------ | ------ | ------ | ---------------------------------- |
| L1        | 0   | accion      | -1       | -1    | 1         | -1     | -1     | 0      | tipo base para acciones primitivas |
| L1        | 1   | direccion   | -1       | -1    | 4         | 0      | 3      | 0      | {norte, sur, este, oeste}          |
| L1        | 2   | instruccion | 0        | -1    | 1         | -1     | -1     | 0      | acción o estructura de control     |
| L1        | 3   | programa    | 2        | -1    | *         | -1     | -1     | 0      | secuencia de instrucciones         |

---
## Tabla de Simbolos

| Línea PRG | Cod | Nombre | Categoría     | Tipo | NumPar | ListaPar | Ámbito | Observaciones                         |
| --------- | --- | ------ | ------------- | ---- | ------ | -------- | ------ | ------------------------------------- |
| L1        | 0   | inicio | palabra_clave | —    | -1     | null     | 0      | marca el inicio del programa          |
| L2        | 1   | mover  | acción        | 0    | 1      | [1]      | 0      | acepta un parámetro de tipo dirección |
| L2        | 2   | norte  | literal       | 1    | -1     | null     | 0      | constante de tipo dirección           |
| L3        | 3   | fin    | palabra_clave | —    | -1     | null     | 0      | fin del bloque principal              |

---

## Secuencia 2:
```
inicio
mover norte
si obstaculo entonces mover este
fin
```

## Tabla de Tipos

| Línea PRG | Cod | Nombre             | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito | Observaciones                              |
| --------- | --- | ------------------ | -------- | ----- | --------- | ------ | ------ | ------ | ------------------------------------------ |
| L1        | 0   | accion             | -1       | -1    | 1         | -1     | -1     | 0      | tipo base para acciones primitivas         |
| L1        | 1   | direccion          | -1       | -1    | 4         | 0      | 3      | 0      | {norte, sur, este, oeste}                  |
| L1        | 2   | condicion          | -1       | -1    | 1         | -1     | -1     | 0      | tipo lógico (booleano)                     |
| L1        | 3   | instruccion        | 0        | -1    | 1         | -1     | -1     | 0      | acción o estructura de control             |
| L1        | 4   | programa           | 3        | -1    | *         | -1     | -1     | 0      | secuencia de instrucciones                 |
| L2        | 5   | bloque_condicional | 3        | -1    | *         | -1     | -1     | 0      | contiene condición y bloque de instrucción |

---

## Tabla de Simbolos

| Línea PRG | Cod | Nombre    | Categoría     | Tipo | NumPar | ListaPar | Ámbito | Observaciones                         |
| --------- | --- | --------- | ------------- | ---- | ------ | -------- | ------ | ------------------------------------- |
| L1        | 0   | inicio    | palabra_clave | —    | -1     | null     | 0      | marca el inicio del programa          |
| L2        | 1   | mover     | acción        | 0    | 1      | [1]      | 0      | acepta un parámetro de tipo dirección |
| L2        | 2   | norte     | literal       | 1    | -1     | null     | 0      | constante de tipo dirección           |
| L3        | 3   | si        | palabra_clave | —    | -1     | null     | 0      | inicio de estructura condicional      |
| L3        | 4   | obstaculo | literal       | 2    | -1     | null     | 0      | literal de tipo condición (booleano)  |
| L3        | 5   | entonces  | palabra_clave | —    | -1     | null     | 0      | separador entre condición y bloque    |
| L3        | 6   | mover     | acción        | 0    | 1      | [1]      | 1      | dentro del bloque condicional         |
| L3        | 7   | este      | literal       | 1    | -1     | null     | 1      | dirección válida                      |
| L4        | 8   | fin       | palabra_clave | —    | -1     | null     | 0      | fin del bloque principal              |
