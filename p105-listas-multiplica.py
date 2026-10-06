# p105-listas-multiplica.py
# Programa que lee dos listas, cada una con 5 elementos numéricos. Crea una tercera lista multiplicando los elementos de las
# dos listas correspondientes. Imprime las tres listas.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles

lista_a = list(map(int, input("Introduzca 5 números para la Lista A: ").split()))
lista_b = list(map(int, input("Introduzca 5 números para la Lista B: ").split()))
lista_c = []

for i in range(5):
    lista_c.append(lista_a[i] * lista_b[i])

print("\n--- RESULTADOS ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C (A * B): {lista_c}")
