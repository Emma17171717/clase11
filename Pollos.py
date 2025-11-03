class Animal:
    def __init__(self, codigo, raza, edad):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad
        self.huevos = []

    def registrar_huevos(self, cantidad):
        self.huevos.append(cantidad)

    def total_huevos(self):
        total = 0
        for n in self.huevos:
            total += n
        return total

    def mostrar_datos(self):
        print("Código:", self.codigo)
        print("Raza:", self.raza)
        print("Edad:", self.edad)
        print("Huevos por semana:", self.huevos)
        print("Total de huevos:", self.total_huevos())
        print()
