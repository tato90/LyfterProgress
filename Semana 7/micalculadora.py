def sumar (a,b):
    return a+b

def restar (a,b):
    return a-b

def multiplicar (a,b):
    return a*b

def division (a,b):
    if (b == 0):
        return "No se puede dividir entre 0"
    else:
        return a/b

def calculadora():
    current_value = None  # Store the current value for consecutive calculations
    print("Seleccione la operacion:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Limpiar")


    while True:
        if current_value is not None:
            print(f"El valor actual es: {current_value}")

        choice = input("Ingresa la operacion a realizar (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            if current_value is None:
                num1 = float(input("Ingresa el primer numero: "))
            else:
                num1 = current_value
            
            num2 = float(input("Ingresa el segundo numero: "))

            if choice == '1':
                current_value = sumar(num1, num2)
            elif choice == '2':
                current_value = restar(num1, num2)
            elif choice == '3':
                current_value = multiplicar(num1, num2)
            elif choice == '4':
                current_value = division(num1, num2)

            print(f"Resultado: {current_value}")

        elif choice == '5':
            current_value = None
            print("El valor ha sido eliminado.")

        else:
            print("Opcion no valida.")

        next_calculation = input("Quiere realizar otra operacionon? (si/no): ")
        if next_calculation.lower() != 'si':
            break

if __name__ == "__main__":
    calculadora()