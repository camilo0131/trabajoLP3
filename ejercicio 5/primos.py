#se define una funcion y toma un argumento(numero)
def es_primo(numero):#se agregan dos puntos(:)
    #verifica si el numero es menor que dos(2)
    if numero < 2:#se agregan dos puntos(:)
        return False
    #itera sobre los numeros desde dos(2)
    for i in range(2, int(numero**0.5) + 1):#se agregan dos puntos(:)
        if numero % i == 0:#se agregan dos puntos(:)
            return False #se corrige la palabra return
    return True
#se pide ingresar el numero entero
limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if es_primo(num)]#se pasa  num como argumento dentro de la funcion(es_primo)
#imprime la lista de numeros primos encontrados
print("Números primos:", primos)

