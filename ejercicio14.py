class Ejercicio14Potencias:
    def __init__(self, numero):
        self.numero = numero
        self.cuadrado = 0
        self.cubo = 0

    def calcular_potencias(self):
        self.cuadrado = self.numero ** 2
        self.cubo = self.numero ** 3

    def mostrar_resultado(self):
        print(f"Número: {self.numero}")
        print(f"Cuadrado: {self.cuadrado}")
        print(f"Cubo: {self.cubo}")


def main():
    numero = float(input("Ingrese un número: "))
    ejercicio = Ejercicio14Potencias(numero)
    ejercicio.calcular_potencias()
    ejercicio.mostrar_resultado()


if __name__ == "__main__":
    main()
