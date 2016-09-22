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
                comparador = 100
                comparadorMax = -100;
                lista = cadena.split(',')
                for num in lista:
                    if int(num) < comparador:
                        comparador = int(num)
                    if int(num) > comparadorMax:
                        comparadorMax = int(num)

                return [tamano, comparador, comparadorMax]

    def processMinMaxProm(self, cadena):
            if cadena == "":
                return [0, 0, 0, 0]
            else:
                tamano = len(cadena.split(','))
                comparador = 100
                comparadorMax = -100;
                lista = cadena.split(',')
                suma = 0
                for num in lista:
                    suma += int(num)
                    if int(num) < comparador:
                        comparador = int(num)
                    if int(num) > comparadorMax:
                        comparadorMax = int(num)

                return [tamano, comparador, comparadorMax, suma/len(lista)]
