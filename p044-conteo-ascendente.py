# p044-conteo-ascendente.py
# Imprimir números de 1 a 100 usando while.

print("\033[2J\033[H", end="")
print("Imprimir números de 1 a 100 usando while.\n")

c = 1
while c <= 100:
    print(f"{c} ", end = "")
    c += 1

print(f"\n\nProceso terminado: {c}")
