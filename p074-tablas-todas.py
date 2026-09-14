# p074-tablas-todas.py
# Imprime las tablas de multiplicar de 1 a 10, del 1 al 10.

print("\033[2J\033[H", end="")
print("Imprime las tablas de multiplicar de 1 a 10, del 1 al 10.\n")

t = int(input("Hasta qué tabla 1 .. t? "))
n = int(input("Hasta dónde 1 .. n? "))

for i in range(1,t+1):
    print(f"Tabla del {i}")

    for j in range(1,n+1):
        print(f"{i} x {j} = {i*j}")

    print()

print("\nProceso terminado.")
