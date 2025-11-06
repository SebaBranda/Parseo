# TT y TS

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
