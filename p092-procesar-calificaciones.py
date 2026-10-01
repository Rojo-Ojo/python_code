# p092-procesar-calificaciones.py
# Procesa n calificaciones entre 1 y 10 en una lista hasta introducir 999.
# al final muestra: la lista, suma, promedio, la más alta, la más baja y
# cuantos alumnos tienen calificaciones mayores al promedio.
# Valida que no introduzca letras en lugar de números.

calificaciones = []
suma = 0

print("\033[2J\033[H", end="")

while True:
    try:
        calificacion = float(input("Ingresa una calificación entre 1 y 10 (o 999 para terminar): "))
        if calificacion == 999:
            break
        elif 1 <= calificacion <= 10:
            calificaciones.append(calificacion)
            suma += calificacion
        else:
            print("Calificación inválida. Debe de estat entre 1 y 10.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

if calificaciones:
    promedio = suma / len(calificaciones)
    calificacion_mas_alta = max(calificaciones)
    calificacion_mas_baja = min(calificaciones)
    alumnos_mayores_promedio = sum(1 for cal in calificaciones if cal > promedio)

    print("\nResultados:")
    print(f"Lista de calificaciones: {calificaciones}")
    print(f"Suma de calificaciones: {suma}")
    print(f"Promedio de calificaciones: {promedio :.2f}")
    print(f"Calificacion mas alta: {calificacion_mas_alta}")
    print(f"Calificación mas baja: {calificacion_mas_baja}")
    print(f"Numero de alumnos con calificacion mayor al promedio: {alumnos_mayores_promedio}")




