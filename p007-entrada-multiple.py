# p007-entrada-multiple.py
# Leer datos múltiples separados por Enter

print("\033[2J\033[H", end="")
print("Dame tres números separados por Enter\n")

n1, n2, n3 = float(input()), float(input()), float(input())

print("Los valores fueron: ")
print(n1, n2, n3)