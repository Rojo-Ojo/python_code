# p079-suma-potencias.py
# Suma las potencias de un número x desde x^1 ... x^n.

print("\033[2J\033[H", end="")
print("Calculando la serie de S = x^1 +... x^n\n")

x = int(input("Número base: "))
n = int(input("Cuántos terminos n: "))
s = 0

print("S= ", end="")
for i in range(1,n+1):
    ta = 1
    for j in range(i):
        ta = ta * x
    print(f"{x}^{i} {"+ " if i<n else ""}", end="")
    s = s + ta
    
print(f"= {s}")