# p036-numeros-consecutivos.py
# Programa que recibe tres números enteros y determina si son consecutivos. 
# Si lo son, muestra un mensaje de confirmación; de lo contrario, informa que no lo son.

print("\033[2J\033[H", end="")
print("Programa que recibe tres números enteros y determina si son consecutivos.\n")

print("Ingresa 3 números separados por espacios: ", end = "")
n1, n2, n3 = map(int, input().split())

if n3 - n2 == 1 and n2 - n1 == 1 :
    print(f"Los números {n1}, {n2}, {n3} son consecutivos en orden ascendente.\n")
elif n1 - n2 == 1 and n2 - n3 == 1 :
    print(f"Los números {n1}, {n2}, {n3} son consecutivos en orden descendente.\n")
else:
    print(f"Los números {n1}, {n2}, {n3} no son consecutivos.\n")
