# p009-promedio-de-calificaciones.py 
# Calcular el promedio de tres calificaciones ingresadas por el usuario.

print("\033[2J\033[H", end="")
print("Calculando el promedio de tres calificaciones. \n")

# Entrada
print("Dame 3 calificaciones separadas por espacio: ")
cal1, cal2, cal3 = input().split()
cal1, cal2, cal3 = float(cal1), float(cal2), float(cal3)

# Proceso
suma = cal1 + cal2 + cal3
promedio = suma / 3

# Salida
print(f"Las calidicaciones son: {cal1}, {cal2}, {cal3}")
print(f"La suma es: {suma:.2f}, \ny el promedio es: {promedio:.2f}")
