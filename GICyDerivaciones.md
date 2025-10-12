## GIC y Derivaciones

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
