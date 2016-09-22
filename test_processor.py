from unittest import TestCase
from processor import Processor

__author__ = 'Daniel Ordonez'


class TestProcessor(TestCase):
    def test_process(self):
        self.assertEqual([0], Processor().process(""), "Numero de elementos cadena vacia")
        self.assertEqual([1], Processor().process("1"), "Numero de elementos cadena 1 numero")
        self.assertEqual([2], Processor().process("0,1"), "Numero de elementos cadena 2 numeros")
        self.assertEqual([4], Processor().process("0,1,2,3"), "Numero de elementos cadena N numeros")

    def test_process2(self):
        self.assertEqual([0, 0], Processor().processMin(""), "Numero de elementos y min cadena vacia")
        self.assertEqual([1, 0], Processor().processMin("0"), "Numero de elementos y min cadena 1 numero")
        self.assertEqual([2, 0], Processor().processMin("1,2"), "Numero de elementos y min cadena 2 numeros")
        self.assertEqual([4, 0], Processor().processMin("0,1,2,3"), "Numero de elementos y min cadena N numeros")

    def test_process3(self):
        self.assertEqual([0, 0, 0], Processor().processMinMax(""), "Numero de elementos y min, max cadena vacia")
        self.assertEqual([1, 0, 0], Processor().processMin("0"), "Numero de elementos y min, max cadena 1 numero")
        # self.assertEqual([2, 0], Processor().processMin("1,2"), "Numero de elementos y min, max cadena 2 numeros")
        # self.assertEqual([4, 0], Processor().processMin("0,1,2,3"), "Numero de elementos y min, max cadena N numeros")
