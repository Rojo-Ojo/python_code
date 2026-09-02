# p052-tabla-conversion.py
# Imprime una tabla de conversión de Peso a Dolar.

tc = 16.80 # Establecemos el tipo de cambio actual.

while True:
    print("\033[2J\033[H", end="")
    print("Tabla de conversión de peso a dolar.\n")
    print("-" * 40)

    while True: # Valida que los valores inicial y final sean correctos.
        inicial = float(input("Valor inicial del rango: "))
        final = float(input("Valor final del rango: "))
        if inicial < final and inicial > 0 and final > 0: break
        else: print("Inicial debe ser menor a final.")

    c = inicial
    print("\nPeso\tDolar")
    print("-" * 40)
    while c <= final:
        print(f"{c:>10.2f}{c/tc:>10.2f}")
        c+=1
        print("-" * 30)

    if input("Deseas Continuar? (S/N)").upper() == "N" : break

print("\nTerminamos de imprimir las tablas.")
