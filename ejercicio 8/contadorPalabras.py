#se define una funcion(contar_palabras_en_archivo) y como argumento(nombre_archivo)
def contar_palabras_en_archivo(nombre_archivo):#se agrega dos puntos(:)
    #se utlizia para encontrar errores al ejecutarse el codigo
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            return len(palabras)#se corrige la palabra return
    except FileNotFoundError:
        return f"El archivo {nombre_archivo} no fue encontrado."
#variable para solicitar ingresar nombre de archivo
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
#se imprime el resultado 
print(f"El archivo contiene {contar_palabras_en_archivo(nombre_archivo)} palabras.")
