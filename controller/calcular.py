from model.calculadora import Calculadora
class Calcular:
    def __init__(self):
        self.sumaTotal = 0
        self.cantidadNumeros = 0
        self.modelo=Calculadora()

    def agregar(self, numero, opcion):
        if opcion:
            self.sumaTotal += numero
            self.cantidadNumeros += 1
        else:
            self.sumaTotal = 0
            self.cantidadNumeros = 0

    def promedio(self):
        if self.cantidadNumeros == 0:
            return 0
        else:
            return self.sumaTotal / self.cantidadNumeros
