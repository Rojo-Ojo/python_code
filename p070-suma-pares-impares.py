# p070-suma-pares-impares.py
# Imprime números pares o impares de 1 a n según lo decidas.

print("\033[2J\033[H", end="")
print("Imprime números pares o impares de 1 a n según lo decidas.\n")
print("[1] Voy de 1 a n con pares.")
print("[2] Voy de 1 a n con impares.")
op = int(input("Elige: "))

suma = 0

if op == 1:
    print("Voy de 1 a n con pares.")
    n = int(input("Hasta dónde? "))
    for x in range(2,n+1,2):
        print(f"{x} ", end="")
        suma = suma + x
    print("\nSuma = "+ str(suma))
elif op == 2:
    print("Voy de 1 a n con impares.")
    n = int(input("Desde dónde? "))
    for x in range(1,n+1,2):
        print(f"{x} ", end="")
        suma = suma + x
    print("\nSuma = "+ str(suma))
else:
    print("\nOpción erronea.")

print("\nProceso terminado.")
