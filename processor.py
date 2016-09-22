__author__ = 'Daniel Ordonez'

class Processor:
    def process(self, cadena):
        if cadena == "":
            return [0]
        else:
            tamano = len(cadena.split(','))
            return [tamano]

    def processMin(self, cadena):
        if cadena == "":
            return [0, 0]
        else:
            tamano = len(cadena.split(','))
            print(tamano)
            return [tamano]
