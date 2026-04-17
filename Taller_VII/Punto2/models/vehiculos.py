class Vehiculo:
    def __init__(self, color, ruedas):
        self.__color = color
        self.__ruedas = ruedas

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not color:
            raise ValueError("El color no puede estar vacio")
        self.__color = color
    
    @property
    def ruedas(self):
        return self.__ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        if ruedas <= 0:
            raise ValueError("El numero de ruedas no puede ser menor o igual a 0")
        self.__ruedas = ruedas

    def __str__(self):
        return f"Vehiculo(color={self.__color}, ruedas={self.__ruedas})"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        if velocidad < 0:
            raise ValueError("La velocidad no puede ser menor a 0")
        self.__velocidad = velocidad

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        if cilindrada <= 0:
            raise ValueError("La cilindrada no puede ser menor o igual a 0")
        self.__cilindrada = cilindrada

    def __str__(self):
        return f"Coche(color = {self.color}, ruedas = {self.ruedas}, velocidad = {self.velocidad}, cilindrada = {self.cilindrada})"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        if not tipo:
            raise ValueError("El tipo no puede estar vacio")
        self.__tipo = tipo  

    def __str__(self):
        return f"Bicicleta(color = {self.color}, ruedas = {self.ruedas}, tipo = {self.tipo})"
    
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.__carga = carga

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga):
        if carga < 0:
            raise ValueError("La carga no puede ser menor a 0")
        self.__carga = carga

    def __str__(self):
        return f"Camioneta(color = {self.color}, ruedas = {self.ruedas}, velocidad = {self.velocidad}, cilindrada = {self.cilindrada}, carga = {self.carga})"
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        if velocidad < 0:
            raise ValueError("La velocidad no puede ser menor a 0")
        self.__velocidad = velocidad

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        if cilindrada <= 0:
            raise ValueError("La cilindrada no puede ser menor o igual a 0")
        self.__cilindrada = cilindrada

    def __str__(self):
        return f"Motocicleta(color = {self.color}, ruedas = {self.ruedas}, tipo = {self.tipo}, velocidad = {self.velocidad}, cilindrada = {self.cilindrada})"
