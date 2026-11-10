# p154-lista-pares.py
# Función que recibe una lista de números enteros y regresa los pares.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def lista_pares(lista: list[int]) -> list[int]:
    """Regresa una lista con los numeros pares de la lista original."""
    pares = [] # lista vacia para almacenar los numeros pares
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero) # agrega el numero par a la lista de pares
    return pares

# Programa principal
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = lista_pares(numeros)
print(f"Los numeros pares de la lista {numeros} son: {resultado}")
