# p026–convertir-temperaturas-v2.py
# Convierte temperaturas de Celcius a Fahrenheit y viceversa.

print("\033[2J\033[H", end="")
print("Convierte temperaturas de Celcius a Fahrenheit y viceversa.\n")
print("[1] Convertir de Fahrenheit a Celcius.")
print("[2] Convertir de Celcius a Fahrenheit.")

op = int(input("Elige: "))

if op == 1:
    print("\nConvirtiendo de Fahrenheit a Celcius")
    f = float(input("Dame la temperatura en grados Fahrenheit: "))
    print(f"\033[FDame la temperatura en grados Fahrenheit: {f}°F")
    c = ( f - 32) * 5/9
    print(f"{f}°F equivalen a {c}°C")
else:
    if op == 2:
        print("\nConvirtiendo de Celcius a Fahrenheit")
        c = float(input("Dame la temperatura en grados Celcius: "))
        print(f"\033[FDame la temperatura en grados Celcius: {c}°C")
        f = ( c * 9/5) + 32
        print(f"{c}°C equivalen a {f}°F")
    else:
        print("\nOpción invalida.")

print("\nPrograma finalizado.")
