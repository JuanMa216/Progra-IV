from .vehiculos import Coche, Bicicleta, Camioneta, Motocicleta
from .objetos import Garaje

def CatalogarVehiculos(vehiculos):
    if not vehiculos:
        print("No hay vehículos en el garaje")
        return

    for vehiculo in vehiculos:
        if isinstance(vehiculo, Camioneta):  
            print(f"Camioneta: {vehiculo.color}, {vehiculo.ruedas}, {vehiculo.velocidad}, {vehiculo.cilindrada}, {vehiculo.carga}")
        elif isinstance(vehiculo, Coche):
            print(f"Coche: {vehiculo.color}, {vehiculo.ruedas}, {vehiculo.velocidad}, {vehiculo.cilindrada}")
        elif isinstance(vehiculo, Motocicleta):  
            print(f"Motocicleta: {vehiculo.color}, {vehiculo.ruedas}, {vehiculo.tipo}, {vehiculo.velocidad}, {vehiculo.cilindrada}")
        elif isinstance(vehiculo, Bicicleta):
            print(f"Bicicleta: {vehiculo.color}, {vehiculo.ruedas}, {vehiculo.tipo}")

def CatalogarVehiculosPorRuedas(vehiculos, ruedas):
    encontrados = [v for v in vehiculos if v.ruedas == ruedas]
    if not encontrados:
        print(f"No hay vehículos con {ruedas} ruedas")
    for vehiculo in encontrados:
        print(f"  {vehiculo}")