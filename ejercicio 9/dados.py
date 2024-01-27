#se importa el modulo (ramdon) de python
import random # se corrige la palabra random
#se define una funcion que toma dos parametros
def simular_lanzamiento_dados(cantidad_dados, caras_por_dado):#se define una funcion
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]
    #Devuelve la lista de lanzamientos aleatorios como resultado 
    return resultados#se corrige la palabra reutrn
#solicita ingresar la cantidad de dados a lanzar
cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
#solicita ingresar la cantidad de caras de cada dado
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))
#se llama a la funcion (simular_lanzamiento_dados) con los valores ingresados y guarda el resultado
lanzamientos = simular_lanzamiento_dados( cantidad_dados,caras_por_dado)#se corrige cuando se llama la funcion agregando (cantidad_dados)
#imprime el resultado
print(f"Resultados del lanzamiento: {lanzamientos}")
