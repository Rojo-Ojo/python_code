# p038-dia-semana.py
# Programa que solicita un número entero del 1 al 7 y muestre el día de la semana correspondiente, 
# considerando que 1 es domingo y 7 es sábado. Si el número ingresado está fuera de ese rango, debe mostrar un mensaje de error.

print("\033[2J\033[H", end="")
print("Programa que solicita un número entero del 1 al 7 y muestre el día de la semana correspondiente.\n")

num = int(input("Dame un número del 1 al 7: "))

if num < 1 or num > 7 :
    print("Error, el número introducido está fuera del rango especificado.\n")
else:
    if num == 1 :
        print("El día es domingo.\n")
    elif num == 2 :
        print("El día es lunes.\n")
    elif num == 3 :
        print("El día es martes.\n")
    elif num == 4 :
        print("El día es miércoles.\n")
    elif num == 5 :
        print("El día es jueves.\n")
    elif num == 6 :
        print("El día es viernes.\n")
    elif num == 7 :
        print("El día es sábado.\n")
