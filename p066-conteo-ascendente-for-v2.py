# p066-conteo-ascendente-for-v2.py
# Números de 1 a n en intervalos de m usando for.

print("\033[2J\033[H", end="")
print("Números de 1 a n en intervalos de m usando for.\n")

n = int(input("Hasta dónde? "))
m = int(input("Intervalos? "))

for i in range(1,n+1,m) :
    print(i)

print("\nProceso terminado.")
