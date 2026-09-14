# p077-factorial-numeros.py
# Calcula el factorial de n números.

print("\033[2J\033[H", end="")
print("Calcula el factorial de n números.\n")

try:
    n = int(input("Hasta qué número? "))

    for x in range(1,n+1):
        print(f"{x}! = ", end="")
        f = 1
        for i in range(1,x+1):
            print(f"{i} {"x" if i<n else ""} ", end="")
            f = f * i

        print(f"= {f:,}")
except ValueError:
    print("Sólo se aceptan números enteros.")
