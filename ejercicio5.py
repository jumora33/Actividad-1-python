class Ejercicio5Operaciones:
    def __init__(self):
        self.suma = 0
        self.x = 20
        self.y = 40

    def ejecutar(self):
        self.suma = self.suma + self.x
        self.x = self.x + (self.y ** 2)
        self.suma = self.suma + (self.x / self.y)

    def mostrar_resultado(self):
        print(f"EL VALOR DE LA SUMA ES: {self.suma}")


def main():
    ejercicio = Ejercicio5Operaciones()
    ejercicio.ejecutar()
    ejercicio.mostrar_resultado()


if __name__ == "__main__":
    main()
