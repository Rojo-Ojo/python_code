# p061-suma-200.py
# Programa que lee números y los suma hasta que el total acumulado sea mayor o igual a 200. 
# Al terminar, muestra cuántos números se introdujeron y la suma final.

while True:
    print("\033[2J\033[H", end="")
    print("Programa que lee números y los suma hasta que el total acumulado sea mayor o igual a 200."
          "\nAl terminar, muestra cuántos números se introdujeron y la suma final.\n")

    sum = cont = 0

    while sum < 200:
        print(f"Suma actual: {sum}. ", end="")
        num = int(input("Introduce un número: "))
        sum += num
        cont += 1

    print("-" * 40)
    print(f"Meta de 200 alcanzada.\nSuma final: {sum}\nTotal de números introducidos: {cont}")
    
    if input("\nDeseas Continuar? (S/N)").upper() == "N" : break
