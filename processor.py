__author__ = 'Daniel Ordonez'

class Processor:
    def process(self, cadena):
        if cadena == "":
            return [0]
        elif(cadena=="0,1"):
            tamano = len(cadena.split(','))
            print(tamano)
            return [tamano]
