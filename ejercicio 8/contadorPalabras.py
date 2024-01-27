def contar_palabras_en_archivo(nombre_archivo):#se agrega dos puntos(:)
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
    except FileNotFoundError:    
            return len(palabras)#se corrige la palabra return
    except Exception as e:
        return f"El archivo {nombre_archivo} no fue encontrado."

archivo_nombre = input("Ingrese el nombre del archivo de texto: ")
print(f"El archivo contiene {contar_palabras_en_archivo(archivo_nombre)} palabras.")
