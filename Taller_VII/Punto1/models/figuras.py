from .calculadora import CalculadoraDeAreas

class Triangulo(CalculadoraDeAreas):
    def __init__(self, base, altura):
        super().__init__(base=base, altura=altura)

    def area(self):
        return 0.5 * self.base * self.altura

    def __str__(self):
        return f"Triangulo(base = {self.base}, altura = {self.altura})"

class Cuadrado(CalculadoraDeAreas):
    def __init__(self, lado):
        super().__init__(lado=lado)

    def area(self):
        return self.lado * self.lado

    def __str__(self):
        return f"Cuadrado(lado = {self.lado})"

class Rectangulo(CalculadoraDeAreas):
    def __init__(self, base, altura):
        super().__init__(base=base, altura=altura)

    def area(self):
        return self.base * self.altura

    def __str__(self):
        return f"Rectangulo(base = {self.base}, altura = {self.altura})"

class Circulo(CalculadoraDeAreas):
    def __init__(self, radio):
        super().__init__(radio=radio)

    def area(self):
        return 3.14159 * self.radio * self.radio

    def __str__(self):
        return f"Circulo(radio = {self.radio})"   