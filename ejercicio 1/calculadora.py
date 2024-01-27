#se define una funcion (calculadora)

def calculadora():

  #se solicita agregar un numero, luego pasa a ser el valor de la variable

    num1 = float (input("Ingrese el primer número: "))   #se agrega un input
    num2 = float (input("Ingrese el segundo número: "))  #se agrega un input
  #define el valor a la operacion a solicitar  
    operacion = (input("Ingrese la operación (+, -, *, /): "))

    if operacion == '+':
        resultado = num1 + num2  #se corrige variable num a num1
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':

        resultado = num1 / num2  #se corrige variable num a num1
    else:
        resultado = "Operación no válida"
  # devuelve el resultado de la función
    return print(resultado) #se agrega un return
calculadora() # se corrige palabra calculadora
 