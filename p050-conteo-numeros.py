# p050-conteo-numeros.py
# El usuario introduce n números, se suman y se cuentan (parar con 999).

print("\033[2J\033[H", end="")
print("El usuario introduce n números, se suman y se cuentan (parar con 999).\n")

c = suma = cp = cn = cz = 0

while True:
    num = int(input("Número: "))
    if num == 999: break
    c += 1
    suma += num
    if num > 0: 
        cp += 1
    elif num < 0: 
        cn += 1
    else: 
        cz += 1

print("\nResumen de cálculos.")
print(f"\nCuantos: {c}")
print(f"Suma: {suma}")
print(f"Positivos: {cp}")
print(f"Negativos: {cn}")
print(f"Ceros: {cz}")

print("\nProceso Terminado.")
