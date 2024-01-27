#se define una funcion
def celsius_a_fahrenheit(celsius):#se agregan dos puntos(:)
    #se calcula la temperatura con una formula de conversion para luego retornar el resultado
    return (celsius * 9/5) + 32 #se agrega el oprador suma(+)
#se solicita agregar la temperatura en grados  celsius
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))#se agrega un input
#se llama a la funcion celsius_a_fahrenheit con la temperatura_celsius para convertir la temperatura ingresada
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
#imprime el resultado convertido
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")
