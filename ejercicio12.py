class Ejercicio12Salario:
    def __init__(self):
        self.horas_trabajadas = 48
        self.valor_hora = 5000
        self.porcentaje_retencion = 12.5
        self.salario_bruto = 0
        self.retencion = 0
        self.salario_neto = 0

    def calcular_salario(self):
        self.salario_bruto = (
            self.horas_trabajadas * self.valor_hora
        )
        self.retencion = (
            self.salario_bruto
            * self.porcentaje_retencion
            / 100
        )
        self.salario_neto = (
            self.salario_bruto - self.retencion
        )

    def mostrar_resultado(self):
        print(f"Salario bruto: ${self.salario_bruto:,.0f}")
        print(f"Retención: ${self.retencion:,.0f}")
        print(f"Salario neto: ${self.salario_neto:,.0f}")


def main():
    ejercicio = Ejercicio12Salario()
    ejercicio.calcular_salario()
    ejercicio.mostrar_resultado()


if __name__ == "__main__":
    main()
