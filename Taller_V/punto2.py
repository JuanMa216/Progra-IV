class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
class Coche_P2(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Bicicleta_P2(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Camion(Coche_P2):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
        
class Motocicleta(Bicicleta_P2):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
def CategoriaVehiculo(vehiculos):
    for vehiculo in vehiculos:
        if isinstance(vehiculo, Camion):
            print("Camion")
        elif isinstance(vehiculo, Coche_P2):
            print("Coche")
        elif isinstance(vehiculo, Motocicleta):
            print("Motocicleta")
        elif isinstance(vehiculo, Bicicleta_P2):
            print("Bicicleta")
        else:
            print("Vehiculo desconocido")
            
def CategoriaVehiculoRuedas(vehiculos, ruedas):
    cantidad_De_Vehiculo_Con_NRuedas = 0
    for vehiculo in vehiculos:
        if vehiculo.ruedas == ruedas:
            print(f"{vehiculo.__class__.__name__} con {ruedas} ruedas")
            cantidad_De_Vehiculo_Con_NRuedas += 1
    print(f"Cantidad de vehículos con {ruedas} ruedas: {cantidad_De_Vehiculo_Con_NRuedas}")