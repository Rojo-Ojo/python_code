# p159-nombres.py
# Función que toma 2 listas de nombres y regresa una lista :
# 1. Nombres que estan en ambas listas.
# 2. Invertir la lista.
# 3. Convertir a mayúsculas.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def capturaNombres() -> list[str]:
    """Captura una lista de nombres del usuario."""
    nombres = []
    while True:
        nombre = input("Nombre (o enter para terminar): ")
        if nombre. lower() == '':
            break
        nombres. append (nombre)
    return nombres

def procesaNombres(lista1: list[str], lista2: list[str]) -> list[str]:
    """Regresa una lista con los nombres que estan en ambas listas, invertidos y en mayusculas."""
    todos = lista1 + lista2
    invertida = todos [: :- 1]
    mayusculas = []
    for i in range(len(invertida)):
        mayusculas.append(invertida[i].upper())
    return mayusculas

nombres1 = ["Ana", "Juan", "Pedro", "Luis", "Maria"]
nombres2 = capturaNombres()
print(f"Los nombres de la primera lista son: {nombres1} - len: {len(nombres1)}")
print(f"Los nombres de la segunda lista son: {nombres2} - len: {len(nombres2)}")
todos = procesaNombres(nombres1, nombres2)
print(f"Los nombres de ambas listas, invertidos y en mayusculas son: {todos} - len: {len(todos)}")
