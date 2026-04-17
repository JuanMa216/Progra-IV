#Calcular el area de al menos 4 figuras geometricas, se deben encapsular los atributos y metodos. Haciendo el uso de clases y herencia.
class CalculadoraDeAreas:
    def __init__(self, radio=None, base=None, altura=None, lado=None):
        self.__radio = radio
        self.__base = base
        self.__altura = altura
        self.__lado = lado

    @property
    def radio(self):
        return self.__radio
    @radio.setter
    def radio(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor a 0")
        self.__radio = radio
    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self, base):
        if base <= 0:
            raise ValueError("La base debe ser mayor a 0")
        self.__base = base
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura):
        if altura <= 0:
            raise ValueError("La altura debe ser mayor a 0")
        self.__altura = altura
    @property
    def lado(self):
        return self.__lado
    @lado.setter
    def lado(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser mayor a 0")
        self.__lado = lado