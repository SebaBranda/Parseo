"""Shim: carga el parser real desde la carpeta `Código/`.

Este archivo mantiene las importaciones existentes para no romper tests ni scripts
que importen `caminante_yacc` desde la raíz. El código real reside en
`Código/caminante_yacc.py` y se carga dinámicamente. Se asegura además de que
el módulo `caminante_lex` (código real) esté disponible en sys.modules antes de
ejecutar el parser, para evitar problemas de import circular.
"""

from importlib.machinery import SourceFileLoader
from importlib import util
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_codigo_dir = (_ROOT / 'Código').resolve()
_lex_path = (_codigo_dir / 'caminante_lex.py')
_yacc_path = (_codigo_dir / 'caminante_yacc.py')

if not _yacc_path.exists():
    raise ImportError(f"No se encontró el parser real en {_yacc_path}")

# Cargar primero el lex desde Código y registrarlo en sys.modules con el nombre
# 'caminante_lex' para que el parser real lo importe correctamente.
if _lex_path.exists():
    _lex_loader = SourceFileLoader('caminante_lex', str(_lex_path))
    _lex_spec = util.spec_from_loader(_lex_loader.name, _lex_loader)
    _lex_module = util.module_from_spec(_lex_spec)
    _lex_loader.exec_module(_lex_module)
    sys.modules['caminante_lex'] = _lex_module

# Ahora cargar el parser real
_loader = SourceFileLoader('caminante_yacc', str(_yacc_path))
_spec = util.spec_from_loader(_loader.name, _loader)
_module = util.module_from_spec(_spec)
_loader.exec_module(_module)
sys.modules['caminante_yacc'] = _module

# Reexportar las funciones/símbolos públicos usados por tests/scripts
parse = getattr(_module, 'parse', None)
parser = getattr(_module, 'parser', None)

__all__ = ['parse', 'parser']
