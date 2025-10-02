| Pila | Entrada | Transición |
|------|---------|------------|
| λ | λ | δ(q0, λ, λ) = (q1, #) |
| # | λ | δ(q1, λ, λ) = (q2, S) |
| #S | λ | δ(q2, λ, S) = (q2, <si> CONDICION <entonces> ACCION <sino> ACCION) |
| #<si> CONDICION <entonces> ACCION <sino> ACCION | <si> | δ(q2, <si>, <si>) = (q2, λ) |
| #CONDICION <entonces> ACCION <sino> ACCION | IDENT COMPARADOR NUMERO | δ(q2, λ, CONDICION) = (q2, IDENT COMPARADOR NUMERO) |
| #IDENT COMPARADOR NUMERO <entonces> ACCION <sino> ACCION | λ | δ(q2, λ, IDENT) = (q2, LETRA IDENT) |
| #LETRA IDENT COMPARADOR NUMERO <entonces> ACCION <sino> ACCION | letra | δ(q2, letra, LETRA) = (q2, λ) |
| #IDENT COMPARADOR NUMERO <entonces> ACCION <sino> ACCION | λ | δ(q2, λ, IDENT) = (q2, LETRA) |
| #COMPARADOR NUMERO <entonces> ACCION <sino> ACCION | <igual_a> | δ(q2, <igual_a>, COMPARADOR) = (q2, λ) |
| #NUMERO <entonces> ACCION <sino> ACCION | λ | δ(q2, λ, NUMERO) = (q2, DIGITO NUMERO) |
| #DIGITO NUMERO <entonces> ACCION <sino> ACCION | dígito | δ(q2, dígito, DIGITO) = (q2, λ) |
| #NUMERO <entonces> ACCION <sino> ACCION | λ | δ(q2, λ, NUMERO) = (q2, DIGITO) |
| #<entonces> ACCION <sino> ACCION | <entonces> | δ(q2, <entonces>, <entonces>) = (q2, λ) |
| #ACCION <sino> ACCION | λ | δ(q2, λ, ACCION) = (q2, <mover> IDENT | <manifestar> CADENA) |
| #<mover> IDENT <sino> ACCION | <mover> | δ(q2, <mover>, <mover>) = (q2, λ) |
| #IDENT <sino> ACCION | λ | δ(q2, λ, IDENT) = (q2, LETRA IDENT) |
| #LETRA IDENT <sino> ACCION | letra | δ(q2, letra, LETRA) = (q2, λ) |
| #IDENT <sino> ACCION | λ | δ(q2, λ, IDENT) = (q2, LETRA) |
| #<sino> ACCION | <sino> | δ(q2, <sino>, <sino>) = (q2, λ) |
| #ACCION | λ | δ(q2, λ, ACCION) = (q2, <mover> IDENT | <manifestar> CADENA) |
| #<manifestar> CADENA | <manifestar> | δ(q2, <manifestar>, <manifestar>) = (q2, λ) |
| #CADENA | λ | δ(q2, λ, CADENA) = (q2, " IDENT ") |
| #" IDENT " | letra | δ(q2, letra, IDENT) = (q2, LETRA IDENT) |
| #LETRA IDENT " | letra | δ(q2, letra, LETRA) = (q2, λ) |
| #IDENT " | λ | δ(q2, λ, IDENT) = (q2, LETRA) |
| #" | " | δ(q2, ", ") = (q2, λ) |
| # | λ | δ(q2, λ, #) = (q3, λ) |
| λ | λ | accept |
| #LETRA | a-z, A-Z | δ(q2, letra, LETRA) = (q2, λ) |
| #DIGITO | 0-9 | δ(q2, dígito, DIGITO) = (q2, λ) |
| #S | λ | δ(q2, λ, S) = (q2, <while> CONDICION <hacer> BLOQUE <fin_while>) |
| #BLOQUE | λ | δ(q2, λ, BLOQUE) = (q2, ACCION BLOQUE | ACCION) |
