# p108-ciudades.py
# Programa que lee nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. 
# Imprime:
# ● Cuántos elementos tiene la lista.
# ● La lista completa.
# ● La lista ordenada en orden descendente.
# ● Cuántas ciudades inician con una letra consonante y sus nombres.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles

ciudades = []
consonantes = []

while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ")

    if ciudad == "$":
        break

    ciudades.append(ciudad)

for ciudad in ciudades:
    primera_letra = ciudad[0].lower()

    if primera_letra not in "aeiou":
        consonantes.append(ciudad)

print("\n--- Resultados ---")
print(f"Total de ciudades introducidas: {len(ciudades)}")
print(f"Lista original: {ciudades}")
print(f"Lista ordenada descendente: {sorted(ciudades, reverse=True)}")
print(f"Ciudades que inician con consonante: {len(consonantes)}")
print(f"Lista de ciudades con consonante inicial: {consonantes}")
