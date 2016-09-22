from unittest import TestCase
from processor import Processor

__author__ = 'Daniel Ordonez'


class TestProcessor(TestCase):
    def test_process(self):
        self.assertEqual([0], Processor().process(""), "Numero de elementos cadena vacia")
        self.assertEqual([1], Processor().process("1"), "Numero de elementos cadena 1 numero")
        self.assertEqual([2], Processor().process("0,1"), "Numero de elementos cadena 2 numeros")
        self.assertEqual([4], Processor().process("0,1,2,3"), "Numero de elementos cadena 2 numeros")
