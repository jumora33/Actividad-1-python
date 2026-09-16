class Ejercicio4EdadFamilia:
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan
        self.edad_alberto = 0
        self.edad_ana = 0
        self.edad_mama = 0

    def calcular_edades(self):
        self.edad_alberto = (2 / 3) * self.edad_juan
        self.edad_ana = (4 / 3) * self.edad_juan
        self.edad_mama = (
            self.edad_juan
            + self.edad_alberto
            + self.edad_ana
        )

    def mostrar_resultado(self):
        print(f"Edad de Juan: {self.edad_juan:.2f} años")
        print(f"Edad de Alberto: {self.edad_alberto:.2f} años")
        print(f"Edad de Ana: {self.edad_ana:.2f} años")
        print(f"Edad de la mamá: {self.edad_mama:.2f} años")


def main():
    edad_juan = float(input("Ingrese la edad de Juan: "))
    if edad_juan <= 0:
        print("La edad debe ser mayor que cero.")
        return

    ejercicio = Ejercicio4EdadFamilia(edad_juan)
    ejercicio.calcular_edades()
    ejercicio.mostrar_resultado()


if __name__ == "__main__":
    main()
