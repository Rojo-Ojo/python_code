# p093-consolidar-ventas.py
# Una empresa tiene 2 sucursales y desea consolidar las ventas de cada una de ellas en una sola lista.
# Se ingresan n ventas para cada sucursal, el usuario lo define.

ventas1 = []
ventas2 = []
ventas_consolidadas = []

print("\033[2J\033[H", end="")
print("¿Cuántas ventas por día se ingresarán en ambas sucursales? ")
n = int(input("Ingrese el número de ventas: "))

# Ingresar ventas para la primera sucursal.
print("\nIngrese las ventas para la primera sucursal: ")
for i in range(n):
    venta = float(input(f"Venta {i + 1}: "))
    ventas1.append(venta)

# Ingresar ventas para la segunda sucursal.
print("\nIngrese las ventas para la segunda sucursal: ")
for i in range(n):
    venta = float(input(f"Venta {i + 1}: "))
    ventas2.append(venta)

# Consolidar las ventas en una sola lista
ventas_consolidadas = ventas1 + ventas2
print("\nVentas consolidadas:")
for i, venta in enumerate(ventas_consolidadas, start=1):
    print(f"Venta {i}: {venta}")

# Total de venas en dinero
total_ventas = sum(ventas_consolidadas)
print(f"\nTotal de ventas: {total_ventas}")
