# p104-procesar-notas.py
# Programa que lee un número indeterminado de notas (calificaciones) entre 0 y 100, se detiene cuando el usuario introduce
# un 0. Valida que todas las notas introducidas estén dentro del rango [0,100].
# Calcula e imprime:
# ● Cuántas notas se introdujeron.
# ● La lista de notas completa.
# ● La suma y el promedio de las notas.
# ● La nota máxima y la nota mínima.
# ● Cuántas notas y cuáles son las notas menores al promedio.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles

notas = []
menores_promedio = []

while True:
    nota = int(input("Introduzca nota (0 para detener): "))
    if nota == 0:
        break
    try:
        if nota < 0 or nota > 100:
            print("\033[F\033[K", end="")
            print(f"Introduzca nota (0 para detener): {nota} <- Entrada inválida, debe ser 0-100")
            continue
        else:
            notas. append (nota)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero para la nota.")

print()

if notas:
    cantidad = len(notas)
    suma = sum(notas)
    promedio = suma / cantidad
    maxima = max(notas)
    minima = min(notas)

    for nota in notas:
        if nota < promedio:
            menores_promedio.append(nota)

print("\n--- RESULTADOS ---")
print(f"Total de notas introducidas: {cantidad}")
print(f"Lista de notas: {notas}")
print(f"Suma de notas: {suma}")
print(f"Promedio de notas: {promedio:.1f}")
print(f"Nota máxima: {maxima}")
print(f"Nota mínima: {minima}")
print(f"Notas menores al promedio ({promedio}): {len(menores_promedio)}")
print(f"Lista de notas menores al promedio: {menores_promedio}")
