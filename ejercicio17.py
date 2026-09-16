import math


class Ejercicio17Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.area = 0
        self.longitud_circunferencia = 0

    def calcular_resultados(self):
        self.area = math.pi * (self.radio ** 2)
        self.longitud_circunferencia = (
            2 * math.pi * self.radio
        )

    def mostrar_resultado(self):
        print(f"Radio: {self.radio:.2f}")
        print(f"Área del círculo: {self.area:.2f}")
        print(
            "Longitud de la circunferencia: "
            f"{self.longitud_circunferencia:.2f}"
        )


def main():
    radio = float(input("Ingrese el radio del círculo: "))
    if radio <= 0:
        print("El radio debe ser mayor que cero.")
        return

    ejercicio = Ejercicio17Circulo(radio)
    ejercicio.calcular_resultados()
    ejercicio.mostrar_resultado()


if __name__ == "__main__":
    main()
