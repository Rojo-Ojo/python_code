# p155-mayor-menor.py
# Se crean 2 funciones una regresa el mayor y otra el menor de una lista de números.
# Se crea una función mas que captura datos del usuario y regresa una lista de números.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def captura_numeros() -> list[float] :
    """Captura números del usuario y regresa una lista de números."""
    numeros = []
    while True:
        entrada = input("Ingrese un número (o 'fin' para terminar): ")
        if entrada. lower() == 'fin':
            break
        try:
            numero = float (entrada)
            numeros.append (numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return numeros

def mayor(lista: list[float]) -> float:
    """Regresa el mayor numero de la lista."""
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

def menor(lista: list[float]) -> float:
    """Regresa el menor numero de la lista."""
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo

# Programa principal
numeros = captura_numeros()
print(f"Los numeros capturados son: {numeros}")
elmasgrade = mayor(numeros)
print(f"El mayor número de la lista es: {elmasgrade}")
elmaspequeno = menor(numeros)
print(f"El menor número de la lista es: {elmaspequeno}")
