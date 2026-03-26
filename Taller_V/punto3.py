class Figura:
    def __init__(self, tipo):
        self.tipo = tipo
    def area(self):
        pass
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return 0.5 * self.base * self.altura
    
class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        import math
        return math.pi * self.radio ** 2