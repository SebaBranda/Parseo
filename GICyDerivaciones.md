## GIC y Derivaciones

```
<programa> ::= INICIO <bloque> FIN

<bloque> ::= <instruccion> <bloque> | ε

<instruccion> ::= <movimiento> 
                | <accion> 
                | <condicional> 
                | <bucle>

<movimiento> ::= MOVER <direccion>
<direccion> ::= NORTE | SUR | ESTE | OESTE

<accion> ::= MANIFESTAR <cadena>

<condicional> ::= SI <expresion> ENTONCES <bloque> <sino_opcional>
<sino_opcional> ::= SINO <bloque> | ε

<bucle> ::= MIENTRAS <expresion> HACER <bloque> FINMIENTRAS

<expresion> ::= <ident> <operador> <valor>
<valor> ::= <numero> | <ident> | <cadena>
<operador> ::= ES_MAYOR_QUE | ES_MENOR_QUE | IGUAL | DISTINTO
```

## Tokens

| Tipo de Token                                       | Ejemplo / Lexema     | Descripción                  |
| --------------------------------------------------- | -------------------- | ---------------------------- |
| `INICIO`                                            | `INICIO`             | Marca de inicio del programa |
| `FIN`                                               | `FIN`                | Marca de fin del programa    |
| `MOVER`                                             | `MOVER`              | Instrucción de movimiento    |
| `NORTE`, `SUR`, `ESTE`, `OESTE`                     | —                    | Direcciones posibles         |
| `MANIFESTAR`                                        | `MANIFESTAR`         | Acción de salida de texto    |
| `SI`, `ENTONCES`, `SINO`                            | —                    | Control condicional          |
| `MIENTRAS`, `HACER`, `FINMIENTRAS`                  | —                    | Control iterativo            |
| `ES_MAYOR_QUE`, `ES_MENOR_QUE`, `IGUAL`, `DISTINTO` | —                    | Operadores relacionales      |
| `IDENT`                                             | Ej. `ruido_ambiente` | Identificadores              |
| `NUM`                                               | Ej. `50`, `1`        | Números                      |
| `CADENA`                                            | Ej. `"Hola"`         | Cadenas literales            |


