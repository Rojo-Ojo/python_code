# p035-tipo-triangulo.py
# Clasificar un triángulo según la longitud de sus lados.

print("\033[2J\033[H", end="")
print("Clasificar un triángulo según la longitud de sus lados.\n")

lado_a = float(input("Longitud del lado a: "))
lado_b = float(input("Longitud del lado b: "))
lado_c = float(input("Longitud del lado c: "))

if lado_a == lado_b and lado_b == lado_c :
    print("\nEs un triángulo equilátero, todos sus lados son iguales.")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c :
    print("\nEs un triángulo isóceles, al menos dos lados son iguales.")
else:
    print("Es un triángulo escaleno, todos sus lados son diferentes.")

print("\nProceso terminado.")
