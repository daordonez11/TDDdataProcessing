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
            comparador = 0
            lista = cadena.split(',')
            for num in lista:
                if num < comparador:
                    comparador = num
            return [tamano, comparador]

    def processMinMax(self, cadena):
            if cadena == "":
                return [0, 0, 0]
            else:
                tamano = len(cadena.split(','))
                print(tamano)
                comparador = 0
                lista = cadena.split(',')
                for num in lista:
                    if num < comparador:
                        comparador = num
                return [tamano, comparador, 0]
