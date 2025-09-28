class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas  

    def calcular_promedio(self):
        return round(sum(self.notas) / len(self.notas), 2)

    def mejor_nota(self):
        return max(self.notas)

    def peor_nota(self):
        return min(self.notas)

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
        print(f"Mejor nota: {self.mejor_nota()}")
        print(f"Peor nota: {self.peor_nota()}")


estudiantes = []

def menu():
    while True:
        print("\n--- MENÚ ESTUDIANTES ---")
        print("1. Agregar estudiante")
        print("2. Información estudiante")
        print("3. Eliminar estudiante")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            notas = []
            for i in range(1, 6):
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota {i}: "))
                        break
                    except ValueError:
                        print("Debes ingresar un número válido para la nota.")
                notas.append(nota)
            estudiantes.append(Estudiante(nombre, notas))
            print("Estudiante agregado con éxito ")

        elif opcion == "2":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                for i, est in enumerate(estudiantes, start=1):
                    print(f"{i}. {est.nombre}")
                try:
                    indice = int(input("Elige el número del estudiante para ver su información: ")) - 1
                    if 0 <= indice < len(estudiantes):
                        print("\n--- INFORMACIÓN DEL ESTUDIANTE ---")
                        estudiantes[indice].imprimir()
                        print("----------------------")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Debes ingresar un número válido.")
            input("\nPresiona Enter para volver al menú...")

        elif opcion == "3":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                for i, est in enumerate(estudiantes, start=1):
                    print(f"{i}. {est.nombre} - Notas: {est.notas}")
                try:
                    indice = int(input("Ingresa el número del estudiante a eliminar: ")) - 1
                    if 0 <= indice < len(estudiantes):
                        eliminado = estudiantes.pop(indice)
                        print(f"Estudiante {eliminado.nombre} eliminado ")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Debes ingresar un número válido.")

        elif opcion == "4":
            print("Gracias por usar el sistema. Programa finalizado.")
            break

        else:
            print("Opción no válida, intenta otra vez.")

menu()