# p156-mayores-promedio.py
# Calculamos el promedio de la lista con funcion
# Creamos una lista con los mayores al promedio con otra funcion

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def promedio(lista: list[float]) -> float:
    """Calcula el promedio de los elementos de una lista de números."""
    suma = 0
    if not lista:
        return 0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def promedio(lista: list[float]) -> float:
    """Calcula el promedio de los elementos de una lista de números."""
    suma = 0
    if not lista:
        return 0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def mayores_al_promedio(lista: list[float], prom: float) -> list[float]:
    """Regresa una lista con los numeros mayores al promedio de la lista original."""
    mayores = []
    for numero in lista:
        if numero > prom:
            mayores. append (numero)
    return mayores

# Programa principal.
numeros = [12.22, 1.5, 2.3, 3.7, 4.1, 10.22, 34.5]
print(f"Los números de la lista son: {numeros}")
prom = promedio(numeros)
print(f"El promedio de los elementos de la lista es: {prom:.2f}")
mayores = mayores_al_promedio(numeros, prom)
print(f"Los numeros mayores al promedio son: {mayores}")
