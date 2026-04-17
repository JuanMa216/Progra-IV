from .calculadora import CalculadoraDeAreas
from .figuras import Circulo, Rectangulo, Triangulo, Cuadrado

def crear_figuras():
    figuras = [
        Circulo(radio=5),
        Rectangulo(base=5, altura=10),
        Triangulo(base=5, altura=10),
        Cuadrado(lado=5)
    ]
    return figuras

def mostrar_figuras(figuras):
    for figura in figuras:
        print(figura)
        if isinstance(figura, Circulo):
            print(f"Area: {figura.area()}")
        elif isinstance(figura, Rectangulo):
            print(f"Area: {figura.area()}")
        elif isinstance(figura, Triangulo):
            print(f"Area: {figura.area()}")
        elif isinstance(figura, Cuadrado):
            print(f"Area: {figura.area()}")
        