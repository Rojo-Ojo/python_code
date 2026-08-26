# p032-aceptar-estudiante.py
# Aceptar estudiantes en base a edad y calificaciones (usando OR).

print("\033[2J\033[H", end="")
print("Aceptar estudiantes en base a edad y calificaciones (usando OR).\n")

nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))

if edad < 18 :
    print(f"\n{nombre}, no aceptamos menores de edad.")
else:
    print("\nContinuamos con el proceso.")
    print("Dame tus dos calificaciones separadas por enter: ")
    c1 = float(input())
    c2 = float(input())
    if c1 < 8 or c2 < 8 :
        print(f"\n{nombre}, no aceptamos calificaciones menores a 8.")
    else:
        print(f"{nombre}, bienvenido a la universidad.")

print("\nProceso terminado.")
