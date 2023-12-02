def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion:\n + = suma\n - = resta\n * = multiplicación\n / = división\n O escriba 'exit' para salir: ") # Menú explicativo en el caso de que un suario no recnozca los símbolos.
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

def ejecutar_operacion(user_input, callback):
    num1, num2, operation = user_input
    if operation == '+':
    elif operation == '-':
    elif operation == '*':
    elif operation == '/':
    else:
        result = "Operacion invalida"
    
    print("Resultado:", result)

def main():
    #Diccionario donde se encuentran las funciones a utilizar
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y:  x * y,
        "/": lambda x, y: x/y
    }

    while True:
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")

        if user_input[2] in operations:
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o  escriba 'exit' para salir.")

if __name__ == "__main__":
    main()

