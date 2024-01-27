#se importan los modulos random & string

import random #se completa la palabra random
import string
#se define una funcion
def  generar_contraseña(longitud=8):# se define generar_contraseña
    #se crea una cadena de caracteres
    caracteres = string.ascii_letters + string.digits + string.punctuation
    #se genera una contraseña
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    #se devuelve la contraseña generada
    return  contraseña #se corrige la palabra return
#se llama a la funcion para imprimir la contraseña
print(generar_contraseña())#se corrige la palabra contraseña
