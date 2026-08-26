# p039-numeros-romanos.py
# Programa que pide al usuario un número entero entre 1 y 10 y muestra su equivalente en números romanos. 
# Si el número está fuera de este rango, debe mostrar un mensaje de error.

print("\033[2J\033[H", end="")
print("Programa que pide al usuario un número entero entre 1 y 10 y muestra su equivalente en números romanos.\n")

num = int(input("Dame un número del 1 al 10: "))

if num < 1 or num > 10 :
    print("Error, el número introducido está fuera del rango especificado.\n")
else:
    if num == 1 :
        print(f"El número {num} en romano es I.\n")
    elif num == 2 :
        print(f"El número {num} en romano es II.\n")
    elif num == 3 :
        print(f"El número {num} en romano es III.\n")
    elif num == 4 :
        print(f"El número {num} en romano es IV.\n")
    elif num == 5 :
        print(f"El número {num} en romano es V.\n")
    elif num == 6 :
        print(f"El número {num} en romano es VI.\n")
    elif num == 7 :
        print(f"El número {num} en romano es VII.\n")
    elif num == 8 :
        print(f"El número {num} en romano es VIII.\n")
    elif num == 9 :
        print(f"El número {num} en romano es IX.\n")
    elif num == 10 :
        print(f"El número {num} en romano es X.\n")
