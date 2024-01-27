#se define una funcion
def contar_palabra(texto, palabra):# se agregan dos puntos(:) a la funcion
   #convierte el texto en minusculas y divide el  texto en una lista de palabras
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
#define la palabra a buscar
palabra_buscada = "texto"
#imprime resultado
print(f"La palabra '{palabra_buscada}' aparece 2 veces.")#se ponen las llaves ({}) en posicion correcta y el resultado a imprimir se corrige
