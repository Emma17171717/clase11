from animal import Animal

class BaseDatos:
    def __init__(self):
        self.pollos = []

    def agregar_pollo(self, codigo, raza, edad):
        nuevo = Animal(codigo, raza, edad)
        self.pollos.append(nuevo)
        print("Pollo agregado correctamente.")

    def mostrar_pollos(self):
        if len(self.pollos) == 0:
            print("No hay pollos registrados.")
        else:
            for pollo in self.pollos:
                pollo.mostrar_datos()

    def actualizar_pollo(self, codigo, nueva_raza, nueva_edad):
        for pollo in self.pollos:
            if pollo.codigo == codigo:
                pollo.raza = nueva_raza
                pollo.edad = nueva_edad
                print("Datos del pollo actualizados.")
                return
        print("No se encontró un pollo con ese código.")

    def eliminar_pollo(self, codigo):
        for pollo in self.pollos:
            if pollo.codigo == codigo:
                self.pollos.remove(pollo)
                print("Pollo eliminado de la base de datos.")
                return
        print("No se encontró un pollo con ese código.")

    def registrar_huevos(self, codigo, cantidad):
        for pollo in self.pollos:
            if pollo.codigo == codigo:
                pollo.registrar_huevos(cantidad)
                print("Producción registrada.")
                return
        print("No se encontró un pollo con ese código.")

    def consultar_pollo(self, codigo):
        for pollo in self.pollos:
            if pollo.codigo == codigo:
                pollo.mostrar_datos()
                return
        print("No se encontró un pollo con ese código.")
