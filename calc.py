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
    #Prints personalizados para cada caso
    num1, num2, operation = user_input
    if operation == '+':
        suma = callback
        resultado = suma(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif operation == '-':
        resta = callback
        resultado1 = resta(num1, num2)
        resultado2 = resta(num2, num1)
        print("El resultado de la resta es:", resultado1,"y el resultado de la resta invertida es:",resultado2)
    elif operation == '*':
        multiplicacion = callback
        resultado = multiplicacion(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif operation == '/':
        division = callback
        if num1 == 0 and num2 == 0: 
            print("No se puede dividir entre cero.")
        elif num1 == 0:
            resultado1 = division(num1, num2)
            print("El resultado de la división es:", resultado1,"y el resultado de la división invertida no se puede al divirse entre cero")
        
        elif num2 == 0:
            resultado1 = division(num2, num1)
            print("No se puede dividir por cero, pero el resultado de la división invertida es:",resultado1)
        else:
            resultado1 = division(num1, num2)
            resultado2 = division(num2, num1)
            print("El resultado de la división es:", resultado1,"y el resultado de la división invertida es:",resultado2)
    else:
        result = "Operacion invalida"

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

