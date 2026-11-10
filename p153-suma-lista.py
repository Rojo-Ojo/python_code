# p153-suma-lista.py
# Función para sumar los elementos de una lista.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def suma_lista(lista: list[float]) -> float:
    """Suma los elementos de una lista de números.'"""
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Programa principal
numeros = [1.5, 2.3, 3.7, 4.1, 10.22]
resultado = suma_lista(numeros)
print(f"La suma de los elementos de la lista {numeros} es: {resultado}")
