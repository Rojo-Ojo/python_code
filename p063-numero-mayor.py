# p063-numero-mayor.py
# Programa que lee una serie de números hasta que el usuario ingrese un 0. 
# Al terminar, el programa muestra cuál fue el número más grande de todos los introducidos.

while True:
    print("\033[2J\033[H", end="")
    print("Programa que lee una serie de números hasta que el usuario ingrese un 0."
          "\nAl terminar, el programa muestra cuál fue el número más grande de todos los introducidos.\n")

    cont = sum = prom = 0
    print("Introduce números (0 para terminar): ")

    i = mayor = 1
    while i != 0:
        i = int(input())
        if i > mayor: mayor = i

    print("-" * 40)
    print(f"El número mayor fue: {mayor}")
    
    if input("\nDeseas Continuar? (S/N)").upper() == "N" : break
