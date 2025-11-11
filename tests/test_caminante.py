import unittest
from caminante_lex import lexer
import caminante_yacc as parser_mod

class TestCaminante(unittest.TestCase):
    def test_simple_program(self):
        data = """
inicio
mover norte
fin
"""
        ok = parser_mod.parse(data)
        self.assertTrue(ok, "Parser should accept simple program")

    def test_conditional_program(self):
        data = """
inicio
si obstaculo entonces
    mover este
fin
"""
        ok = parser_mod.parse(data)
        self.assertTrue(ok, "Parser should accept conditional program")

if __name__ == '__main__':
    unittest.main()
