# p060-promedio-suma.py
# Programa que lee números introducidos por el usuario hasta que ingrese un 0. 
# Al finalizar, muestra el conteo total de números, la suma y el promedio de la serie.

while True:
    print("\033[2J\033[H", end="")
    print("Programa que lee números introducidos por el usuario hasta que ingrese un 0."
          "\nAl finalizar, muestra el conteo total de números, la suma y el promedio de la serie.\n")

    cont = sum = prom = 0
    print("Introduce números (0 para terminar): ")

    i = 1
    while i != 0:
        i = int(input())
        sum += i
        if i != 0: cont += 1

    print("-" * 40)
    print(f"Se introdujeron {cont} números.\nLa suma es: {sum}\nEl promedio es: {sum/cont:.2f}")
    
    if input("\nDeseas Continuar? (S/N)").upper() == "N" : break
