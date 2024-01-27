

def calculadora():
   
    num1 = float (input("Ingrese el primer número: "))
    num2 = float (input("Ingrese el segundo número: "))
    operacion = (input("Ingrese la operación (+, -, *, /): "))

    if operacion == '+':
        resultado = num1 + num2 
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2 
    else:
        resultado = "Operación no válida"

    return print(resultado) 

calculadora() 

 