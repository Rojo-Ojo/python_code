# p045-conteo-ascendente-v2.py
# Imprimir números de 1 a n usando while.

print("\033[2J\033[H", end="")
print("Imprimir números de 1 a 100 usando while.\n")

n = int(input("Hasta dónde? "))
m = int(input("Incrementos? ")) 

c = m
while c <= n:
    print(f"{c} ", end = "")
    c += m

print(f"\n\nProceso terminado: {c}")
