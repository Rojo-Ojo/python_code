# p127-contar-caracteres.py
# ● Programa que pide al usuario que ingrese una cadena de texto.
# ● Crea un diccionario vacío para almacenar la frecuencia (cantidad de apariciones) de cada carácter.
# ● Itera sobre cada carácter en la cadena ingresada.
# ● En cada iteración:
#   o Si el carácter no existe como llave en el diccionario, agrégalo con un valor de 1.
#   o Si el carácter ya existe, incrementa su valor actual en 1.
# ● Al finalizar el ciclo, muestra el diccionario resultante con el conteo de caracteres.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

cadena = input("Ingrese una cadena: ")

frecuencia = {}

for caracter in cadena:
    if caracter not in frecuencia:
        frecuencia[caracter] = 1
    else:
        frecuencia[caracter] += 1

print("Resultado:")
print(frecuencia)
