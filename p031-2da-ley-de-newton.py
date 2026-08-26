# p031-2da-ley-de-newton.py
# Calcular los valores de la 2da Ley de Newton.

print("\033[2J\033[H", end="")
print("Calcular los valores de la 2da Ley de Newton.\n")

print("[F] Fuerza      ( f = m * a )")
print("[M] Masa        ( m = f / a )")
print("[A] Aceleración ( f = m * a )")
print("Elige: ")
op = input().upper()

f = m = a = 0

if op == "F" :
    print("\nCalculando la Fuerza.")
    m = float(input("Dame la masa (kg): "))
    a = float(input("Dame la aceleración (m/s\u00b2): "))
    f = m * a
    print(f"\nLa fuerza es: {f:.4f} N")
elif op == "M" :
    print("\nCalculando la Masa.")
    f = float(input("Dame la fuerza (N): "))
    a = float(input("Dame la aceleración (m/s\u00b2): "))
    m = f / a
    print(f"\nLa masa es: {m:.4f} kg")
elif op == "A" :
    print("\nCalculando la Aceleración.")
    f = float(input("Dame la fuerza (N): "))
    m = float(input("Dame la masa (kg): "))
    a = f / m
    print(f"\nLa aceleración es: {a:.4f} mm/s\u00b2")
else:
    print("\nOpción incorrecta.")

print("\nProceso terminado.")