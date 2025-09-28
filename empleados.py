class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Sueldo: {self.sueldo:.2f}")

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

    def aumento(self, porcentaje):
        self.sueldo += self.sueldo * (porcentaje / 100)
        print(f"Sueldo aumentado en {porcentaje}%. Nuevo sueldo: {self.sueldo:.2f}")


empleados = []

def menu():
    while True:
        print("\n--- MENÚ EMPLEADOS ---")
        print("1. Agregar empleado")
        print("2. Consultar empleado")
        print("3. Aumentar sueldo")
        print("4. Eliminar empleado")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            try:
                sueldo = float(input("Ingrese el sueldo: "))
            except ValueError:
                print("Debes ingresar un número válido para el sueldo.")
                continue
            empleados.append(Empleado(nombre, sueldo))
            print("Empleado agregado con éxito ")

        elif opcion == "2":
            if not empleados:
                print("No hay empleados registrados.")
            else:
                for i, emp in enumerate(empleados, start=1):
                    print(f"{i}. {emp.nombre}")
                try:
                    indice = int(input("Elige el número del empleado a consultar: ")) - 1
                    if 0 <= indice < len(empleados):
                        print("\n--- INFORMACIÓN DEL EMPLEADO ---")
                        print(f"Nombre: {empleados[indice].nombre}")
                        print(f"Sueldo: {empleados[indice].sueldo:.2f}")
                        empleados[indice].paga_impuestos()
                        print("----------------------")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Debes ingresar un número válido.")
            input("\nPresiona Enter para volver al menú...")

        elif opcion == "3":
            if not empleados:
                print("No hay empleados registrados.")
            else:
                for i, emp in enumerate(empleados, start=1):
                    print(f"{i}. {emp.nombre} - Sueldo: {emp.sueldo:.2f}")
                try:
                    indice = int(input("Elige el número del empleado para aumentar sueldo: ")) - 1
                    if 0 <= indice < len(empleados):
                        porc = float(input("Ingrese el porcentaje de aumento: "))
                        empleados[indice].aumento(porc)
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Debes ingresar un número válido.")

        elif opcion == "4":
            if not empleados:
                print("No hay empleados registrados.")
            else:
                for i, emp in enumerate(empleados, start=1):
                    print(f"{i}. {emp.nombre} - Sueldo: {emp.sueldo:.2f}")
                try:
                    indice = int(input("Ingresa el número del empleado a eliminar: ")) - 1
                    if 0 <= indice < len(empleados):
                        eliminado = empleados.pop(indice)
                        print(f"Empleado {eliminado.nombre} eliminado ")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Debes ingresar un número válido.")

        elif opcion == "5":
            print("Gracias por usar el sistema. Programa finalizado.")
            break

        else:
            print("Opción no válida, intenta otra vez.")

menu()