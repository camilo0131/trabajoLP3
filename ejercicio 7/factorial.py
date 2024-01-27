def factorial(n):#se agrega dos puntos(:)
   if n == 0 or n == 1: #se corrige == 
      return  1 #se define return
   else:
      return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}")#se pone numero como argumento
