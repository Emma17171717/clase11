from bd_Pollos import BaseDatos

def main():
    bd = BaseDatos()

    while True:
        print("=== SISTEMA DE CONTROL DE POLLOS ===")
        print("1. Agregar pollo")
        print("2. Mostrar todos los pollos")
        print("3. Actualizar datos de un pollo")
        print("4. Eliminar pollo")
        print("5. Registrar producción de huevos")
        print("6. Consultar pollo")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del pollo: ")
            raza = input("Raza: ")
            edad = input("Edad (en semanas): ")
            bd.agregar_pollo(codigo, raza, edad)

        elif opcion == "2":
            bd.mostrar_pollos()

        elif opcion == "3":
            codigo = input("Código del pollo a actualizar: ")
            raza = input("Nueva raza: ")
            edad = input("Nueva edad: ")
            bd.actualizar_pollo(codigo, raza, edad)

        elif opcion == "4":
            codigo = input("Código del pollo a eliminar: ")
            bd.eliminar_pollo(codigo)

        elif opcion == "5":
            codigo = input("Código del pollo: ")
            cantidad = int(input("Huevos producidos esta semana: "))
            bd.registrar_huevos(codigo, cantidad)

        elif opcion == "6":
            codigo = input("Código del pollo: ")
            bd.consultar_pollo(codigo)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
        print()
main()
