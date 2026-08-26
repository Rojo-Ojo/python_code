# p041-aceptar-estudiante-v2.py
# Programa que solicita el nombre, sexo (h/m), edad y tres calificaciones de un aspirante. 
# El programa evalúa los datos y muestra un mensaje claro que indica si el estudiante fue aceptado. 
# Si no es aceptado, el mensaje debe especificar la razón del rechazo (ya sea por no cumplir con el sexo, la edad o el promedio requerido).
# La "Universidad Kitty Kat SA" solo acepta estudiantes que cumplan con los siguientes requisitos: ser
# mujer, ser mayor de 21 años y tener un promedio entre 8 y 9.5.

print("\033[2J\033[H", end="")
print("Programa que solicita el nombre, sexo (h/m), edad y tres calificaciones de un aspirante.\n" \
"Con esto evalúa si es elegible o no para ingreso a la Universidad Kitty Kat SA.\n")

nombre = input("Nombre: ")
sexo = input("Sexo (h/m): ")

if sexo == "m" or sexo == "M" :
    edad = int(input("Edad: "))
    if edad > 21 :
        print("Calificaciones: ", end = "")
        c1, c2, c3 = map(float, input().split())
        prom = (c1+c2+c3) / 3
        if prom >= 8 and prom <= 9.5 :
            print("Estudiante aceptada.\n")
        else:
            print("Estudiante rechazada, no cumple con el promedio especificado.\n")
    else:
        print("Estudiante rechazada, no cumple con la edad mínima.\n")
else:
    print("Estudiante rechazado, esta universidad es sólo para mujeres.\n")
