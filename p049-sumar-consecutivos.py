# p049-sumar-consecutivos.py
# Suma números hasta que el total sea >= 5000.

print("\033[2J\033[H", end="")
print("Suma números hasta que el total sea >= 5000.\n")

c = 0
s = 0

while c <= 200:
    c += 1
    s += c
    print(f"{c} ")
    if s >= 5000: break

print(f"La suma es {s} despues de {c} números.")
