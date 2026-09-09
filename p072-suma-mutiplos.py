# p072-suma-mutiplos.py
# Imprime números de 1 a n, sólo los múltiplos de m.

print("\033[2J\033[H", end="")
print("Imprime números de 1 a n, sólo los múltiplos de m.\n")

m = int(input("Qué múltiplos quieres? "))
n = int(input("Iniciando en 1 hasta dónde? "))

c = s = 0

for i in range(1,n+1):
    if i % m == 0:
        print(f"{i} ", end="")
        c += 1
        s += i

print(f"\n\nCuántos múltiplos fueron? {c}")
print(f"Suma de los múltiplos de {m} = {s}")
