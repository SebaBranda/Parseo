"""Parser para el lenguaje Caminante usando PLY (yacc).
Conecta con `caminante_lex.py` (lexer) y emplea la GIC encontrada en `GICyDerivaciones.md`.

Provee la función `parse(data)` que devuelve True si el parse tuvo éxito (sin errores sintácticos),
False en caso contrario.
"""

from __future__ import annotations
import sys
from typing import Any

# Importar el lexer y tokens
from caminante_lex import lexer as lex_lexer
from caminante_lex import tokens as lex_tokens

import ply.yacc as yacc

# PLY espera una variable global `tokens`
tokens = lex_tokens

# Parse result state
_parse_ok = True

# Gramática basada en GICyDerivaciones.md y README.md

def p_program(p):
    'program : INICIO bloque FIN'
    p[0] = ('program', p[2])

# Bloque: definimos una lista de instrucciones (left-recursive) para reducir ambigüedades
def p_bloque(p):
    'bloque : instrucciones'
    p[0] = p[1]


def p_instrucciones_recursive(p):
    'instrucciones : instrucciones instruccion'
    p[0] = p[1] + [p[2]]


def p_instrucciones_single(p):
    'instrucciones : instruccion'
    p[0] = [p[1]]


def p_instrucciones_empty(p):
    'instrucciones : '
    p[0] = []


def p_instruccion(p):
    '''instruccion : movimiento
                   | accion
                   | condicional
                   | bucle
                   | declaracion'''
    p[0] = p[1]


# movimiento: MOVER direccion
def p_movimiento(p):
    'movimiento : MOVER direccion'
    p[0] = ('mover', p[2])


def p_direccion(p):
    '''direccion : NORTE
                 | SUR
                 | ESTE
                 | OESTE'''
    p[0] = ('dir', p[1])


# accion: MANIFESTAR CADENA
def p_accion_manifestar(p):
    'accion : MANIFESTAR CADENA'
    # p[2] es la cadena lexeme con comillas; dejamos tal cual
    p[0] = ('manifestar', p[2])


# condicional: SI expresion ENTONCES bloque (SINO bloque)?
def p_condicional(p):
    'condicional : SI expresion ENTONCES bloque sino_opcional'
    # p: 1=SI 2=expresion 3=ENTONCES 4=bloque 5=sino_opcional
    p[0] = ('si', p[2], p[4], p[5])


def p_sino_opcional_sino(p):
    'sino_opcional : SINO bloque'
    p[0] = p[2]


def p_sino_opcional_empty(p):
    'sino_opcional : '
    p[0] = None


# bucle: MIENTRAS expresion HACER bloque FINMIENTRAS
# o: REPETIR NUM VECES COLON bloque  (soporte adicional)

def p_bucle_mientras(p):
    'bucle : MIENTRAS expresion HACER bloque FINMIENTRAS'
    p[0] = ('mientras', p[2], p[4])


def p_bucle_repite(p):
    'bucle : REPETIR NUM VECES COLON bloque'
    p[0] = ('repite', p[2], p[5])


# Declaracion/Asignacion simple: establece IDENT a valor
def p_declaracion(p):
    'declaracion : ESTABLECE IDENT A valor'
    p[0] = ('decl', p[2], p[4])


# expresion: IDENT operador valor
# operador: ES_MAYOR_QUE | ES_MENOR_QUE | IGUAL | DISTINTO | ES
# Para reducir conflictos, `valor` NO incluye IDENT; IDENT se trata en la produccion de expresion.
def p_expresion_compare(p):
    'expresion : IDENT operador valor'
    p[0] = ('expr', p[2], ('ident', p[1]), p[3])


def p_expresion_ident(p):
    'expresion : IDENT'
    p[0] = ('ident', p[1])


def p_expresion_valor(p):
    'expresion : valor'
    p[0] = p[1]


def p_operador(p):
    '''operador : ES_MAYOR_QUE
                 | ES_MENOR_QUE
                 | IGUAL
                 | DISTINTO
                 | ES'''
    p[0] = p[1]


def p_valor_num(p):
    'valor : NUM'
    p[0] = ('num', p[1])


def p_valor_cadena(p):
    'valor : CADENA'
    p[0] = ('cadena', p[1])


# Error handling
def p_error(p):
    global _parse_ok
    _parse_ok = False
    if p:
        print(f"Syntax error at token {p.type} (value={p.value!r}) line {p.lineno}")
    else:
        print("Syntax error at EOF")


# Construir parser
parser = yacc.yacc()


def parse(data: str) -> bool:
    """Parsea la entrada `data`. Devuelve True si no hubo errores sintácticos."""
    global _parse_ok
    _parse_ok = True
    # resetear lexer linea
    lex_lexer.lineno = 1
    try:
        parser.parse(data, lexer=lex_lexer)
    except Exception as e:
        print('Parsing exception:', e)
        _parse_ok = False
    return _parse_ok


if __name__ == '__main__':
    sample = '''\ninicio\nmover norte\nsi obstaculo entonces\n    mover este\nfin\n'''
    print('Entrada de prueba:\n', sample)
    ok = parse(sample)
    print('\nParse OK:', ok)
