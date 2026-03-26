class Transporte():
    
    def __init__(self, capacidad, tarifa):
        self.capacidad = capacidad
        self.tarifa = tarifa
        
    def calcularPasaje(self, distancia):
        pass
    
class Taxi(Transporte):
    
    def __init__(self, capacidad, tarifa, tipo):
        super().__init__(capacidad, tarifa)
        self.tipo = tipo
        
    def calcularPasaje(self, distancia):
        return self.tarifa * distancia

class Bus(Transporte):
    
    def __init__(self, capacidad, tarifa, ruta):
        super().__init__(capacidad, tarifa)
        self.ruta = ruta
        
    def calcularPasaje(self, distancia):
        return self.tarifa + (distancia * 0.5)
    
class Metro(Transporte):
    
    def __init__(self, capacidad, tarifa, linea):
        super().__init__(capacidad, tarifa)
        self.linea = linea
        
    def calcularPasaje(self, distancia):
        return self.tarifa * distancia
    