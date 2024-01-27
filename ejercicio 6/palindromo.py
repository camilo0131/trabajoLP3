#se define una funcion(es_palindromo) y como argumento (texto)
def es_palindromo(texto):#se agrega dos putnos(:)
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
   #devuelve el valor de la funcion 
    return texto == texto[::-1]
#se solicita ingresar palabra
palabra_frase = input("Ingrese una palabra o frase: ")
#se ejecuta el codigo si la condicion es verdadera
if es_palindromo(palabra_frase):# se le agrega el argumento
    print(f"{palabra_frase} es un palíndromo.") 
#se ejecuta si la condicion en if es falsa
else:
    print(f"{palabra_frase} no es un palíndromo.")
