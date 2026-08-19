# p008-entrada-con-espacio.py
# Leer datos múltiplos separados por un espacio u otro carácter.

print("\033[2J\033[H", end="")
print("Dame tres números separados por un espacio.\n")

n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

print("Los valores introducidos son: ")
print(n1, n2, n3)