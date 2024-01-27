#se define una funcion la cual toma dos parametros
def calcular_precio_con_descuento(precio_base, porcentaje_descuento):#se define una funcion y se le agrega dos puntos (:)
    #calcula el monto tomando el precio base
    descuento = precio_base * (porcentaje_descuento / 100)
    #calcula el precio final restando el descuento
    precio_final = precio_base - descuento
   #devuelve el precio final del producti
    return precio_final# se corrige la palabra return

#solicita ingresar el precio del producto
precio_base = float(input("Ingrese el precio base del producto:"))#se agrega un input
#se solicita ingresar el porcentaje de descuento
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
#se llama a la funcion (calcular_precio_con_descuento) con los valores ingresados y guarda el resultado en la variable(precio final)
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)
#imprime el precio final del producto
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")
