# p037-numero-mayor.py
# Programa que recibe tres números enteros e identifica y muestra cuál de ellos es el mayor.

print("\033[2J\033[H", end="")
print("Programa que recibe tres números enteros e identifica y muestra cuál de ellos es el mayor.\n")

print("Ingresa 3 números separados por espacios: ", end = "")
n1, n2, n3 = map(int, input().split())

if n1 > n2 and n1 > n3 :
    print(f"El mayor es {n1}.\n")
elif n2 > n1 and n2 > n3 :
    print(f"El mayor es {n2}.\n")
else :
    print(f"El mayor es {n3}.\n")
