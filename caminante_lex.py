"""Shim: carga el módulo real desde la carpeta `Código/`.

Este archivo mantiene las importaciones existentes para no romper tests ni scripts
que importen `caminante_lex` desde la raíz. El código real reside en
`Código/caminante_lex.py` y se carga dinámicamente.
"""

from importlib.machinery import SourceFileLoader
from importlib import util
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_codigo_path = (_ROOT / 'Código' / 'caminante_lex.py').resolve()

if not _codigo_path.exists():
    raise ImportError(f"No se encontró el módulo real en { _codigo_path }")

# Cargar el módulo real y registrarlo en sys.modules bajo el nombre original
loader = SourceFileLoader('caminante_lex', str(_codigo_path))
spec = util.spec_from_loader(loader.name, loader)
module = util.module_from_spec(spec)
loader.exec_module(module)
sys.modules['caminante_lex'] = module

# Reexportar símbolos importantes
lexer = getattr(module, 'lexer', None)
tokens = getattr(module, 'tokens', None)

__all__ = ['lexer', 'tokens']
