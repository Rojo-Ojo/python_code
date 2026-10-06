# p106-mes-día-nombre.py
# Programa que lee un número de mes (ej. 4). Guarda los días de cada mes en una lista y los nombres de los meses en otra
# lista. Asume 28 días para febrero. Imprime el nombre del mes y la cantidad de días del mes correspondiente (ej. marzo, 30).

print("\033c", end="") # Esto limpia la consola en sistemas compatibles

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input("Introduzca un número de mes (1-12): "))

print("\n--- RESULTADOS ---")
print(f"Mes: {meses[mes - 1]}")
print(f"Días: {dias[mes - 1]}")
