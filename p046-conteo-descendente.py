# p046-conteo-descendente.py
# Imprimir números de 100 a 1 usando while.

print("\033[2J\033[H", end="")
print("Imprimir números de 100 a 1 usando while.\n")

c = 100
while c >= 1:
    print(f"{c} ", end = "")
    c -= 1

print(f"\n\nProceso terminado: {c}")
