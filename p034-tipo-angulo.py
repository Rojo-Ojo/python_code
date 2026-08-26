# p034-tipo-angulo.py
# Dado un ángulo en el rango de 0 a 360 indicar que tipo de ángulo es.

print("\033[2J\033[H", end="")
print("Dado un ángulo en el rango de 0 a 360 indicar que tipo de ángulo es.\n")

ang = int(input("Ángulo: "))

if ang >= 0 and ang <= 360 :
    print("Tu ángulo es: ", end = "")
    if ang < 90 : 
        print("AGUDO")
    elif ang == 90 : 
        print("RECTO")
    elif ang > 90 : 
        print("OBTUSO")
    elif ang == 180 : 
        print("LLANO")
    elif ang > 180 : 
        print("CONCAVO")
    elif ang == 360 : 
        print("CERRADO")
else:
    print("Ángulo fuera de rango.")

print("\nProceso terminado.")
