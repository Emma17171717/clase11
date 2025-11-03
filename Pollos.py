class Animal:
    def __init__(self, codigo, raza, edad):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad
        self.huevos_semana = []

    def registrar_produccion(self, cantidad):
        self.huevos_semana.append(cantidad)

    def produccion_total(self):
        return sum(self.huevos_semana)

    def mostrar_info(self):
        print(f"Código: {self.codigo}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} semanas")
        print(f"Huevos por semana: {self.huevos_semana}")
        print(f"Producción total: {self.produccion_total()} huevos\n")
