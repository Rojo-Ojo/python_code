# p071-suma-promedio-numeros.py
# Calcula la suma y el promedio de n calificaciones.

while True:
    print("\033[2J\033[H", end="")
    print("Calcula la suma y el promedio de n calificaciones.\n")

    n = int(input("Cuántas calificaciones? "))
    suma = 0
    strcals = ""
    for i in range(1,n+1,1):
        cal = int(input(f"Calificación {i} : "))
        suma += cal
        strcals = strcals + str(cal) + " "

    print(f"\nLos números fueron: {strcals}")
    print(f"La suma es: {suma}")
    print(f"El promedio es: {suma/n}")
    if input("\nSeguimos (S/N) ?").upper()=="N":break
