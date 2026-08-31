# p047-conteo-descendente-v2.py
# Imprimir números de n a 1 usando while.

print("\033[2J\033[H", end="")
print("Imprimir números de n a 1, en intervalos de m, usando while.\n")

n = int(input("Desde dónde? "))
m = int(input("Decremento? ")) 

c = n
while c >= 1:
    print(f"{c} ", end = "")
    c -= m

print(f"\n\nProceso terminado: {c}")