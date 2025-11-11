import unittest
import caminante_yacc as parser_mod

class TestCaminanteExtra(unittest.TestCase):
    def test_repite_program(self):
        data = """
inicio
repite 3 veces: 
    mover este
fin
"""
        ok = parser_mod.parse(data)
        self.assertTrue(ok)

    def test_mientras_program(self):
        data = """
inicio
mientras contador es_mayor_que 0 hacer
    mover norte
finmientras
fin
"""
        ok = parser_mod.parse(data)
        self.assertTrue(ok)

    def test_decimal_and_string(self):
        data = """
inicio
establece x a 3.14
manifestar "Valor: \\\"hola\\\""
fin
"""
        ok = parser_mod.parse(data)
        # Parser doesn't implement 'establece' semantic node but should lex/parse structure
        self.assertTrue(ok)

    def test_comments_ignored(self):
        data = """
# comentario de linea
inicio
// otro comentario
mover sur
fin
"""
        ok = parser_mod.parse(data)
        self.assertTrue(ok)

if __name__ == '__main__':
    unittest.main()
