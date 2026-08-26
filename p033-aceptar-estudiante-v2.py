# p033-aceptar-estudiante-v2.py
# Aceptar estudiantes en base a edad y calificaciones (usando AND).

print("\033[2J\033[H", end="")
print("Aceptar estudiantes en base a edad y calificaciones (usando AND).\n")

nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))

if edad >= 18 :
    print("\nContinuamos con el proceso.")
    print("Dame tus dos calificaciones separadas por enter: ")
    c1 = float(input())
    c2 = float(input())
    if c1 > 7 and c2 > 7 :
        print(f"{nombre}, bienvenido a la universidad.")
    else:
        print(f"\n{nombre}, no aceptamos calificaciones menores a 8.")
else:
    print(f"\n{nombre}, no aceptamos menores de edad.")

print("\nProceso terminado.")
