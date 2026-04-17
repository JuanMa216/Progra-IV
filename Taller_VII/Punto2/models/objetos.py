from .vehiculos import Coche, Bicicleta, Camioneta, Motocicleta

def Garaje():
    vehiculos = [
        Coche("rojo", 4, 120, 1600),
        Bicicleta("azul", 2, "montaña"),
        Camioneta("negro", 6, 100, 2500, 1000),
        Motocicleta("verde", 2, "deportiva", 180, 600)
    ]

    print("\nVehículos en el garaje:")
    for vehiculo in vehiculos:
        print(vehiculo)

    return vehiculos