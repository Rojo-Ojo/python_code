# p034-tipo-angulo-V2.py
# Dado un ángulo en el rango de 0 a 360 indicar que tipo de ángulo es.

print("\033[2J\033[H", end="")
print("Dado un ángulo en el rango de 0 a 360 indicar que tipo de ángulo es.\n")

ang = int(input("Ángulo: "))

if ang < 0 or ang > 360 :
    print("Ángulo fuera de rango.")
else:
    print("Tu ángulo es: ", end = "")
    if ang < 90 : 
        print("AGUDO")
    elif ang == 90 : 
        print("RECTO")
    elif ang < 180 : 
        print("OBTUSO")
    elif ang == 180 : 
        print("LLANO")
    elif ang < 360 : 
        print("CONCAVO")
    elif ang == 360 : 
        print("CERRADO")

print("\nProceso terminado.")
