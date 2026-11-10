# p157-pares-impares.py
# Recibe una lista de números y regresa 2 listas, una de pares, otra de impares.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def separar_pares_impares(lista: list[int]) -> tuple[list[int], list[int]]:
    """Separa los números pares e impares de la lista original y regresa dos listas."""
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares. append (numero)
        else:
            impares.append (numero)
    return pares, impares

# Programa principal.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Los números de la lista son: {numeros}")
p, i = separar_pares_impares (numeros)
print(f"Los numeros pares son: {p}")
print(f"Los números impares son: {i}")
