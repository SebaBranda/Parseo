UNIVERSIDAD NACIONAL DE HURLINGHAM
## Inst. de Tecnología e Ingeniería
### PARSEO Y GENERACIÓN DE CÓDIGO
#### Prof: Mag. Ing. Pablo Pandolfo
#### Examen Parcial - Noviembre 2025

* **ALUMNO**: Brandariz Sebastián
* **DNI**: 25647424

#### NOTA: EL EXAMEN ESCRITO ES UN DOCUMENTO DE GRAN IMPORTANCIA PARA LA EVALUACIÓN DE LOS CONOCIMIENTOS ADQUIRIDOS, POR LO TANTO, SE SOLICITA LEER ATENTAMENTE LO SIGUIENTE

* Responda claramente cada punto, detallando con la mayor precisión posible lo solicitado.
* Sea prolijo y ordenado en el desarrollo de los temas.
* Sea cuidadoso con las faltas de ortografía y sus oraciones.
* No desarrollar el examen en lápiz.
* Aprobación del examen: Con nota mayor o igual a 4 (cuatro)
* Condiciones de aprobación: 60%
* Duración de examen: 3 horas.

---

1. **[2.5 puntos]** Diséñese el diagrama de transiciones para un scanner del lenguaje cuyas palabras verifican las siguientes restricciones:  
    * Una cadena comando es el nombre del comando seguido de uno o más espacios en blanco, y a continuación una lista de parámetros que puede ser vacía.  
    * Un comando es una secuencia no vacía de cadenas comando separadas por un delimitador.  
    * Un delimitador es un elemento del conjunto `{ . , ; }`.  
    * Un nombre comienza con una letra y sigue con cero o más letras o dígitos. La lista de parámetros es una secuencia de uno o más nombres separados por uno o más espacios en blanco.


<img width="886" height="477" alt="image" src="https://github.com/user-attachments/assets/80da1e18-37ca-49af-aada-d5cb5450679a" />


n: nombre
d: digito
s: espacio
p: parámetro
Delimitadores: {. , ;}

---

2. **[1 punto]** Analícese la entrada: **run test1 test2;build main;deploy**

Estado = q0
Entrada = 'r' (letra)
Estado = q1
Entrada = 'u' (letra)
Estado = q1
Entrada = 'n' (letra)
Estado = q1
Entrada = ' ' (espacio)
Token = COMANDO
Lexema = "run"
Retroceso = 1

Estado = q0
Entrada = ' ' (espacio)
Estado = q3
Entrada = 't' (letra)
Token = ESPACIO
Lexema = " "
Retroceso = 1

Estado = q0
Entrada = 't' (letra)
Estado = q1
Entrada = 'e' (letra)
Estado = q1
Entrada = 's' (letra)
Estado = q1
Entrada = 't' (letra)
Estado = q1
Entrada = '1' (digito)
Estado = q1
Entrada = ' ' (espacio)
Token = PARAMETRO
Lexema = "test1"
Retroceso = 1

Estado = q0
Entrada = ' ' (espacio)
Estado = q3
Entrada = 't' (letra)
Token = ESPACIO
Lexema = " "
Retroceso = 1

Estado = q0
Entrada = 't' (letra)
Estado = q1
Entrada = 'e' (letra)
Estado = q1
Entrada = 's' (letra)
Estado = q1
Entrada = 't' (letra)
Estado = q1
Entrada = '2' (digito)
Estado = q1
Entrada = ';' (delimitador)
Token = PARAMETRO
Lexema = "test2"
Retroceso = 1

Estado = q0
Entrada = ';' (delimitador)
Estado = q2
Token = DELIMITADOR
Lexema = ";"
Retroceso = 0

Estado = q0
Entrada = 'b' (letra)
Estado = q1
Entrada = 'u' (letra)
Estado = q1
Entrada = 'i' (letra)
Estado = q1
Entrada = 'l' (letra)
Estado = q1
Entrada = 'd' (letra)
Estado = q1
Entrada = ' ' (espacio)
Token = COMANDO
Lexema = "build"
Retroceso = 1

Estado = q0
Entrada = ' ' (espacio)
Estado = q3
Entrada = 'm' (letra)
Token = ESPACIO
Lexema = " "
Retroceso = 1

Estado = q0
Entrada = 'm' (letra)
Estado = q1
Entrada = 'a' (letra)
Estado = q1
Entrada = 'i' (letra)
Estado = q1
Entrada = 'n' (letra)
Estado = q1
Entrada = ';' (delimitador)
Token = PARAMETRO
Lexema = "main"
Retroceso = 1

Estado = q0
Entrada = ';' (delimitador)
Estado = q2
Token = DELIMITADOR
Lexema = ";"
Retroceso = 0

Estado = q0
Entrada = 'd' (letra)
Estado = q1
Entrada = 'e' (letra)
Estado = q1
Entrada = 'p' (letra)
Estado = q1
Entrada = 'l' (letra)
Estado = q1
Entrada = 'o' (letra)
Estado = q1
Entrada = 'y' (letra)
Estado = q1
Token = COMANDO
Lexema = "deploy"
Retroceso = 0

---

3. **[1.5 puntos]** Impleméntese scanner en PLY

```Python
import ply.lex as lex

# Tokens
tokens = ('COMANDO', 'PARAMETRO', 'DELIMITADOR', 'ESPACIO')

# Estado para controlar contexto
es_primer_nombre = True

def t_COMANDO_PARAMETRO(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    global es_primer_nombre
    
    if es_primer_nombre:
        t.type = 'COMANDO'
        es_primer_nombre = False
    else:
        t.type = 'PARAMETRO'
    
    return t

def t_DELIMITADOR(t):
    r'[.,;]'
    global es_primer_nombre
    es_primer_nombre = True
    return t

def t_ESPACIO(t):
    r'\s+'
    return t

t_ignore = ''

def t_error(t):
    print(f"Carácter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def analizar_entrada(entrada):
    global es_primer_nombre
    es_primer_nombre = True
    
    lexer.input(entrada)
    tokens = []
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value))
    
    return tokens

# Probar la entrada
entrada = "run test1 test2;build main;deploy"
resultados = analizar_entrada(entrada)

print("Tokens generados:")
for token in resultados:
    print(f"{token[0]:<12} '{token[1]}'")

```

---

4. **[2.5 puntos]** Compruébese si la siguiente GIC es LL(1), mostrando los conjuntos PRIM, SIG y PRED.

$$P \\rightarrow \\{L$$
$$L \\rightarrow \\} \\mid S;L$$
$$S \\rightarrow V = E$$
$$V \\rightarrow a \\mid b \\mid c$$
$$E \\rightarrow V O$$
$$O \\rightarrow + V \\mid - V \\mid V$$

```python
PRIM(P) = { { }
PRIM(L) = { }, a, b, c }
PRIM(S) = { a, b, c }
PRIM(V) = { a, b, c }
PRIM(E) = { a, b, c }
PRIM(O) = { +, -, a, b, c }

SIG(P) = { $ }
SIG(L) = { $ }
SIG(S) = { ; }
SIG(V) = { =, +, -, a, b, c, ; }
SIG(E) = { ; }
SIG(O) = { ; }

PRED(P,{) = P→{L
PRED(L,}) = L→}
PRED(L,a) = L→S;L
PRED(L,b) = L→S;L
PRED(L,c) = L→S;L
PRED(S,a) = S→V=E
PRED(S,b) = S→V=E
PRED(S,c) = S→V=E
PRED(V,a) = V→a
PRED(V,b) = V→b
PRED(V,c) = V→c
PRED(E,a) = E→VO
PRED(E,b) = E→VO
PRED(E,c) = E→VO
PRED(O,+) = O→+V
PRED(O,-) = O→-V
PRED(O,a) = O→V
PRED(O,b) = O→V
PRED(O,c) = O→V

```
## Tabla de Análisis

|   | {     | }   | ; | = | a | b | c | + | - | $ |
|---|---    |---  |---|---|---|---|---|----|---|----|
| P | P→{L  |     |   |   |   |   |   |    |   |    |
| L |       | L→} |   |   | L→S;L | L→S;L | L→S;L |    |   |    |
| S |       |     |   |   | S→V=E | S→V=E | S→V=E |    |   |    |
| V |       |     |   |   | V→a | V→b | V→c |    |   |    |
| E |       |     |   |   | E→VO | E→VO | E→VO |    |   |    |
| O |       |     |   |   | O→V | O→V | O→V | O→+V | O→-V |    |
```python
Para L:
PRED(L → }) ∩ PRED(L → S ; L) = { } ∩ { a, b, c } = ∅

Para V:
PRED(V → a) ∩ PRED(V → b) = { a } ∩ { b } = ∅
PRED(V → a) ∩ PRED(V → c) = { a } ∩ { c } = ∅
PRED(V → b) ∩ PRED(V → c) = { b } ∩ { c } = ∅

Para O:
PRED(O → + V) ∩ PRED(O → - V) = { + } ∩ { - } = ∅
PRED(O → + V) ∩ PRED(O → V)  = { + } ∩ { a, b, c } = ∅
PRED(O → - V) ∩ PRED(O → V)  = { - } ∩ { a, b, c } = ∅

```
Todas las intersecciones entre los conjuntos PRED de las producciones de un mismo no terminal son vacías.
Por lo tanto, la gramática es LL(1).

---

5. **[1 punto]** Muéstrese los movimientos realizados por el ASDP LL(1) con la entrada: **{a = a + b; b = c}**
```
Parcial                   | Entrada                          | Acción 
--------------------------+----------------------------------+-----------------------
[P $]                     | { a = a + b ; b = c }            | Inicial
['{', L, $]               | { a = a + b ; b = c }            | P → { L
[L, $]                    | a = a + b ; b = c }              | Emparejar '{'
['S',';','L',$]           | a = a + b ; b = c }              | L → S ; L
['V','=','E',';','L',$]   | a = a + b ; b = c }              | S → V = E
['a','=', 'E',';','L',$]  | a = a + b ; b = c }              | V → a
['=','E',';','L',$]       | a = a + b ; b = c }              | Emparejar 'a'
['E',';','L',$]           | = a + b ; b = c }                | Emparejar '='
['V','O',';','L',$]       | a + b ; b = c }                  | E → V O
['a','O',';','L',$]       | a + b ; b = c }                  | V → a
['O',';','L',$]           | + b ; b = c }                    | Emparejar 'a'
['+','V',';','L',$]       | + b ; b = c }                    | O → + V
['V',';','L',$]           | b ; b = c }                      | Emparejar '+'
['b',';','L',$]           | b ; b = c }                      | V → b
[';','L',$]               | ; b = c }                        | Emparejar 'b'
['L',$]                   | b = c }                          | Emparejar ';'
['S',';','L',$]           | b = c }                          | L → S ; L
['V','=','E',';','L',$]   | b = c }                          | S → V = E
['b','=','E',';','L',$]   | b = c }                          | V → b
['=','E',';','L',$]       | = c }                            | Emparejar 'b'
['E',';','L',$]           | c }                              | Emparejar '='
['V','O',';','L',$]       | c }                              | E → V O
['c','O',';','L',$]       | c }                              | V → c
['O',';','L',$]           | }                                | Emparejar 'c'
['O',';','L',$]           | }                                | **M[O, '}'] = ∅**
(rechazo)                 | }                                | **Estado de rechazo**
```
---

6. **[1.5 puntos]** Impleméntese parser en PLY

```python
import ply.lex as lex
import ply.yacc as yacc

# ==================== LEXER ====================
tokens = (
    'LLAVE_IZQ', 'LLAVE_DER', 'PUNTO_COMA', 'IGUAL',
    'MAS', 'MENOS', 'ID'
)

t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_PUNTO_COMA = r';'
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_ID = r'[a-c]'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# ==================== PARSER ====================
class ParserPredictivo:
    def __init__(self):
        self.tokens = tokens
        self.precedence = ()
        
        # Tabla PRED basada en nuestro análisis
        self.tabla_pred = {
            'P': {'{': ['LLAVE_IZQ', 'L']},
            'L': {
                '}': ['LLAVE_DER'],
                'a': ['S', 'PUNTO_COMA', 'L'],
                'b': ['S', 'PUNTO_COMA', 'L'], 
                'c': ['S', 'PUNTO_COMA', 'L']
            },
            'S': {
                'a': ['V', 'IGUAL', 'E'],
                'b': ['V', 'IGUAL', 'E'],
                'c': ['V', 'IGUAL', 'E']
            },
            'V': {
                'a': ['ID'],
                'b': ['ID'],
                'c': ['ID']
            },
            'E': {
                'a': ['V', 'O'],
                'b': ['V', 'O'],
                'c': ['V', 'O']
            },
            'O': {
                'a': ['V'],
                'b': ['V'],
                'c': ['V'],
                '+': ['MAS', 'V'],
                '-': ['MENOS', 'V']
            }
        }
    
    def p_sentencia(self, p):
        '''sentencia : P'''
        p[0] = p[1]
        print("✓ Análisis completado")
    
    def p_P(self, p):
        '''P : LLAVE_IZQ L'''
        p[0] = ('P', p[2])
        print("P → {L")
    
    def p_L_cerrar(self, p):
        '''L : LLAVE_DER'''
        p[0] = ('L', '}')
        print("L → }")
    
    def p_L_continuar(self, p):
        '''L : S PUNTO_COMA L'''
        p[0] = ('L', p[1], p[3])
        print("L → S;L")
    
    def p_S(self, p):
        '''S : V IGUAL E'''
        p[0] = ('S', p[1], p[3])
        print("S → V=E")
    
    def p_V(self, p):
        '''V : ID'''
        p[0] = ('V', p[1])
        print(f"V → {p[1]}")
    
    def p_E(self, p):
        '''E : V O'''
        p[0] = ('E', p[1], p[2])
        print("E → VO")
    
    def p_O_suma(self, p):
        '''O : MAS V'''
        p[0] = ('O', '+', p[2])
        print("O → +V")
    
    def p_O_resta(self, p):
        '''O : MENOS V'''
        p[0] = ('O', '-', p[2])
        print("O → -V")
    
    def p_O_v(self, p):
        '''O : V'''
        p[0] = ('O', p[1])
        print("O → V")
    
    def p_error(self, p):
        if p:
            print(f"Error de sintaxis en '{p.value}' (tipo: {p.type})")
        else:
            print("Error de sintaxis: EOF inesperado")

# Construir parser
parser_obj = ParserPredictivo()
parser = yacc.yacc(module=parser_obj)

# Prueba
if __name__ == "__main__":
    entrada = "{ a = a + b ; b = c }"
    print(f"Analizando: {entrada}")
    print("=" * 40)
    resultado = parser.parse(entrada)
    print(f"Resultado: {resultado}")
```

EOF
