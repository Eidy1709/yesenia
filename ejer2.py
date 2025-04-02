def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

while True:
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        operator = input("Ingresa el operador (+, -, *, /): ")

        if operator == '+':
            print("Resultado: ", add(num1, num2))
        elif operator == '-':
            print("Resultado: ", subtract(num1, num2))
        elif operator == '*':
            print("Resultado: ", multiply(num1, num2))
        elif operator == '/':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print("Resultado: ", result)
        else:
            print("Operador inválido")

        continue_calc = input("¿Quieres hacer otro cálculo? (sí/no): ")
        if continue_calc.lower() != 'sí':
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingresa valores numéricos.")