"""Ejecutor simple para scanner y parser dentro de la carpeta `Código`.

Uso:
  python main.py scan [archivo]
  python main.py parse [archivo]
  python main.py both [archivo]

Si no se proporciona `archivo`, se usa una muestra interna.
"""

import argparse
import os
import sys


SAMPLE = '''
inicio
mover norte
si obstaculo entonces
    mover este
fin
'''


def run_scanner(text):
    from caminante_lex import lexer
    lexer.lineno = 1
    lexer.input(text)
    for tok in lexer:
        print(f"Token: {tok.type}, Valor: {tok.value}, Línea: {tok.lineno}")


def run_parser(text):
    from caminante_yacc import parse
    # parse devuelve True/False según si hubo errores sintácticos
    ok = parse(text)
    print('\nParse correcto:' if ok else '\nParse con errores:')
    return ok


def main():
    ap = argparse.ArgumentParser(description='Ejecutar scanner y parser (Código)')
    sub = ap.add_subparsers(dest='cmd')

    p_scan = sub.add_parser('scan', help='Ejecutar sólo el scanner')
    p_scan.add_argument('file', nargs='?', help='Archivo a escanear')

    p_parse = sub.add_parser('parse', help='Ejecutar sólo el parser')
    p_parse.add_argument('file', nargs='?', help='Archivo a parsear')

    p_both = sub.add_parser('both', help='Ejecutar scanner y parser en secuencia')
    p_both.add_argument('file', nargs='?', help='Archivo de entrada')

    args = ap.parse_args()
    args = ap.parse_args()

    def get_text(path):
        if path:
            if not os.path.exists(path):
                print(f"No se encontró el archivo: {path}")
                return None
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return SAMPLE

    if args.cmd is not None:
        path = getattr(args, 'file', None)
        text = get_text(path)
        if text is None:
            sys.exit(1)
        if args.cmd == 'scan':
            run_scanner(text)
        elif args.cmd == 'parse':
            run_parser(text)
        elif args.cmd == 'both':
            print('--- Scanner ---')
            run_scanner(text)
            print('\n--- Parser ---')
            run_parser(text)
        return

    # Interfaz interactiva si no se pasaron argumentos: esperar selección del usuario
    def ask(prompt):
        try:
            return input(prompt)
        except EOFError:
            try:
                # Intentar leer directamente desde la consola en Windows
                with open('CON', 'r', encoding='utf-8', errors='ignore') as con:
                    print(prompt, end='', flush=True)
                    return con.readline()
            except Exception:
                print('\nEntrada no interactiva disponible. Usa los subcomandos: scan/parse/both <archivo>')
                return ''

    while True:
        print('\nSelecciona una opción:')
        print('  1) Scanner')
        print('  2) Parser')
        print('  3) Ambos (Scanner + Parser)')
        print('  4) Salir')
        choice = ask('Opción (1-4): ').strip()
        if choice == '4' or choice.lower() in ('q', 'quit', 'salir'):
            print('Saliendo.')
            break

        if choice not in ('1', '2', '3'):
            print('Opción no válida. Intenta de nuevo.')
            continue
        path = ask('Archivo (dejar vacío para usar la muestra interna): ').strip()
        text = get_text(path if path != '' else None)
        if text is None:
            continue

        if choice == '1':
            run_scanner(text)
        elif choice == '2':
            run_parser(text)
        elif choice == '3':
            print('--- Scanner ---')
            run_scanner(text)
            print('\n--- Parser ---')
            run_parser(text)


if __name__ == '__main__':
    main()
