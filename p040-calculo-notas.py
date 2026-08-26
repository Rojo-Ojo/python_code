# p040-calculo-notas.py
# Programa que calcula el promedio de 5 calificaciones ingresadas por el usuario. 
# Basado en el promedio, el programa deberá mostrar un mensaje.

print("\033[2J\033[H", end="")
print("Programa que calcula el promedio de 5 calificaciones ingresadas por el usuario.\n")

print("Ingresa 5 calificaciones separadas por espacios: ", end = "")
c1, c2, c3, c4, c5 = map(float, input().split())
prom = (c1+c2+c3+c4+c5) / 5

if prom <= 10 and prom >= 9 :
    print(f"Promedio: {prom:.2f}\nPerfecto, tu esfuerzo valió la pena.")
elif prom < 9 and prom >= 8 :
    print(f"Promedio: {prom:.2f}\nExcelente, sigue así.")
elif prom < 8 and prom >= 7 :
    print(f"Promedio: {prom:.2f}\nMuy bien, puedes mejorar.")
elif prom < 7 and prom >= 6 :
    print(f"Promedio: {prom:.2f}\nPasas de panzazo.")
else:
    print(f"Promedio: {prom:.2f}\nQuedas reprobado")
