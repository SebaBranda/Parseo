"""Scanner (lex) para el lenguaje Caminante.

Alineado con los tokens/gramática de los documentos del repo (GICyDerivaciones.md, README.md).
Genera tokens en mayúscula que espera el parser (p. ej. MOVER, INICIO, FIN, IDENT, NUM, CADENA...).

Dependencia: ply (pip install ply)
"""

import ply.lex as lex

# Tokens básicos
tokens = [
    'IDENT',
    'NUM',
    'CADENA',
    'COLON',
]

# Palabras reservadas (lexema -> NOMBRE_DE_TOKEN)
reserved = {
    # Estructura / control
    'inicio': 'INICIO',
    'fin': 'FIN',
    'si': 'SI',
    'entonces': 'ENTONCES',
    'sino': 'SINO',
    'repite': 'REPETIR',
    'veces': 'VECES',
    'mientras': 'MIENTRAS',
    'hacer': 'HACER',
    'finmientras': 'FINMIENTRAS',

    # Acciones / palabras clave del lenguaje
    'mover': 'MOVER',
    'manifestar': 'MANIFESTAR',
    'interactuar_con': 'INTERACTUAR_CON',
    'transicionar_a': 'TRANSICIONAR_A',

    # Direcciones (se tratan como literales/tokens específicos)
    'norte': 'NORTE',
    'sur': 'SUR',
    'este': 'ESTE',
    'oeste': 'OESTE',

    # Operadores y comparadores
    'es_mayor_que': 'ES_MAYOR_QUE',
    'es_menor_que': 'ES_MENOR_QUE',
    'igual': 'IGUAL',
    'distinto': 'DISTINTO',
    'es': 'ES',

    # Otros (desde README / Scanner.md)
    'establece': 'ESTABLECE',
    'a': 'A',
    'y': 'Y',
    'mas': 'MAS',
    'menos': 'MENOS',
    'multiplicado_por': 'MULTIPLICADO_POR',
    'dividido_por': 'DIVIDIDO_POR',
    'esta_presente_en': 'ESTA_PRESENTE_EN',
}

# Añadir las palabras reservadas a la lista de tokens que reconoce PLY
tokens = tokens + list(set(reserved.values()))

# Reglas simples (expresiones regulares)
t_COLON = r':'

# Cadena entre comillas dobles (con escapes)
t_CADENA = r'"([^"\\]|\\.)*"'

# Ignorar espacios y tabs (newlines manejados aparte)
t_ignore = ' \t\r'


def t_NUM(t):
    r"\d+(\.\d+)?"
    # convertir a int cuando sea entero, float cuando tenga punto
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Usar case-insensitive matching: las palabras reservadas en los docs están en minúsculas
    key = t.value.lower()
    if key in reserved:
        t.type = reserved[key]
    else:
        t.type = 'IDENT'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Comentarios de una línea con // o # (se ignoran)
def t_comment(t):
    r'(//.*)|(\#.*)'
    pass


# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)


# Analizador léxico
lexer = lex.lex()


if __name__ == '__main__':
    # Ejemplo tomado/ajustado de README/Scanner.md
    data = '''
inicio
mover norte
si obstaculo entonces mover este
fin
'''
    print('--- Entrada de prueba ---')
    print(data)
    lexer.input(data)
    print('\n--- Tokens generados ---')
    for tok in lexer:
        print(f'Token: {tok.type}, Valor: {tok.value}, Línea: {tok.lineno}')
