from unittest import TestCase
from processor import Processor

__author__ = 'Daniel Ordonez'


class TestProcessor(TestCase):
    def test_process(self):
        self.assertEqual([0], Processor().process(""), "Numero de elementos cadena vacia")
