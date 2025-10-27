# calculadora.py
from operaciones import suma, resta, multiplicacion, division

def calculadora():
    continuar = "s"

    while continuar.lower() == "s":
        try:
            # Pedir los dos números
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            # Elegir la operación
            print("\n¿Qué operación deseas realizar?")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")

            opcion = input("Selecciona (1-4): ")

            # Ejecutar según la opción
            if opcion == "1":
                resultado = suma(num1, num2)
            elif opcion == "2":
                resultado = resta(num1, num2)
            elif opcion == "3":
                resultado = multiplicacion(num1, num2)
            elif opcion == "4":
                resultado = division(num1, num2)
            else:
                print("Opción no válida.")
                continue

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Por favor, introduce solo números válidos.")

        # Preguntar si quiere continuar
        continuar = input("\n¿Quieres hacer otra operación? (s/n): ")

    print("¡Hasta luego!")


if __name__ == "__main__":
    calculadora()
