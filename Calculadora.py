def calculadora():
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        opcion = input("Elige una opción (1/2/3/4): ")

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if opcion == '1':
                print(f"{num1} + {num2} = {num1 + num2}")

            elif opcion == '2':
                print(f"{num1} - {num2} = {num1 - num2}")

            elif opcion == '3':
                print(f"{num1} * {num2} = {num1 * num2}")

            elif opcion == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: División por cero no permitida.")

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

        continuar = input("¿Quieres realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            break

calculadora()
