md
### Derivación a Izq. para 'si-entonces'

Basados en la GIC:

'Programa -> Instruccion | Instruccion Programa'

'Instruccion -> Condicional'

'Condicional -> si <Condicion>, entonces <Bloque> sino <Bloque> | si <Condicion>, entonces <Bloque>'

'<Condicion> -> ID es_mayor_que NUM'

'<Bloque> -> mover "dir" | manifestar "mensaje"'

'ID -> 'ruido_ambiente''

'NUM -> '50''

Para:

'si ruido_ambiente es_mayor_que 50, entonces:
    mover "este"
sino:
    manifestar "Demasiado ruido."'

Prog (Regla 1)

Instruccion

Instruccion (Regla 2)

- Condicional

Condicional (Regla 3)

- si <Condicion>, entonces <Bloque> sino <Bloque>

si <Condicion>, entonces <Bloque> sino <Bloque> (Regla 4)

- si ID es_mayor_que NUM, entonces <Bloque> sino <Bloque>

si ID es_mayor_que NUM, entonces <Bloque> sino <Bloque> (Regla 6)

- si ruido_ambiente es_mayor_que NUM, entonces <Bloque> sino <Bloque>

si ruido_ambiente es_mayor_que NUM, entonces <Bloque> sino <Bloque> (Regla 7)

- si ruido_ambiente es_mayor_que 50, entonces <Bloque> sino <Bloque>

si ruido_ambiente es_mayor_que 50, entonces <Bloque> sino <Bloque> (Regla 5)

- si ruido_ambiente es_mayor_que 50, entonces mover "dir" sino <Bloque>

si ruido_ambiente es_mayor_que 50, entonces mover "dir" sino <Bloque> (Regla 5)

- si ruido_ambiente es_mayor_que 50, entonces mover "dir" sino manifestar "mensaje"

si ruido_ambiente es_mayor_que 50, entonces mover "dir" sino manifestar "mensaje"

- si ruido_ambiente es_mayor_que 50, entonces mover "este" sino manifestar "Demasiado ruido."

### Derivación a Der:

Prog (Regla 1)

- Instruccion

Instruccion (Regla 2)

- Condicional

Condicional (Regla 3)

- si <Condicion>, entonces <Bloque> sino <Bloque>

si <Condicion>, entonces <Bloque> sino <Bloque> (Regla 5)

- si <Condicion>, entonces <Bloque> sino manifestar "mensaje"

si <Condicion>, entonces <Bloque> sino manifestar "mensaje" (Regla 5)

- si <Condicion>, entonces mover "dir" sino manifestar "mensaje"

si <Condicion>, entonces mover "dir" sino manifestar "mensaje" (Regla 4)

- si ID es_mayor_que NUM, entonces mover "dir" sino manifestar "mensaje"

si ID es_mayor_que NUM, entonces mover "dir" sino manifestar "mensaje" (Regla 7)

- si ID es_mayor_que 50, entonces mover "dir" sino manifestar "mensaje"

si ID es_mayor_que 50, entonces mover "dir" sino manifestar "mensaje" (Regla 6)

- si ruido_ambiente es_mayor_que 50, entonces mover "dir" sino manifestar "mensaje"

- si ruido_ambiente es_mayor_que 50, entonces mover "dir" sino manifestar "mensaje"

- si ruido_ambiente es_mayor_que 50, entonces mover "este" sino manifestar "Demasiado ruido."

