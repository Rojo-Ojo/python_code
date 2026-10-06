# p110-comprension-filtra-palabras.py
# Programa que, dada una lista de palabras introducidas por el usuario separadas por espacios, utilizaa comprensión de listas
# para crear una nueva lista que contenga solo aquellas palabras que tengan más de 4 caracteres y convertirlas a
# mayúsculas. Imprime la lista original y la lista filtrada.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles

palabras = input("Introduzca varias palabras separadas por espacios: ").split()
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 4]

print("\n--- Resultados ---")
print(f"Lista original: {palabras}")
print(f"Lista filtrada: {palabras_filtradas}")
