#define funcion (factorial)
def factorial(n):#se agrega dos puntos(:)
   #se ejecuta el codigo si la condicion es verdadera
   if n == 0 or n == 1: #se corrige == 
      return  1 #se define return
   #se ejecuta si la condicion en if es falsa
   else:
   #retorna el resultado 
      return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))
#imprime resultado
print(f"El factorial de {numero} es {factorial(numero)}")#se pone numero como argumento
