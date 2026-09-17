# p080-compara-rendimiento-inversion.py
# Programa que compara el crecimiento de dos fondos de inversión a lo largo de varios años. El usuario debe ingresar el monto inicial y 
# la tasa de interés anual (porcentaje) para cada uno de los dos fondos, así como el número de años a proyectar. El programa muestra una 
# tabla comparativa anual y al final indica qué fondo generó un mayor rendimiento.

print("\033[2J\033[H", end="")
print("Programa que compara el crecimiento de dos fondos de inversión a lo largo de varios años. El usuario debe ingresar el monto inicial y\n"
      "la tasa de interés anual (porcentaje) para cada uno de los dos fondos, así como el número de años a proyectar. El programa muestra una\n"
      "tabla comparativa anual y al final indica qué fondo generó un mayor rendimiento.\n")

print("\n--- Fondo de Inversión A --")
monto_a = float(input("Monto inicial: "))
interes_a = float(input("Tasa de interés anual (%): "))

print("\n--- Fondo de Inversión B --")
monto_b = float(input("Monto inicial: "))
interes_b = float(input("Tasa de interés anual (%): "))

anios = int(input("\nAños a proyectar: "))

print("\n--- Comparación de Rendimientos Anuales ---")
print(f"{'Año':<5}| {'Fondo A':<12}| {'Fondo B':<12}")
print("-" * 43)

for i in range(1, anios+1):
    monto_a *= (1 + (interes_a/100))
    monto_b *= (1 + (interes_b/100))
    print(f"{i:<5}| $ {monto_a:<10.2f}| $ {monto_b:<10.2f}")

if monto_a > monto_b:
    print(f"\nResultado final: El Fondo A (${monto_a:.2f}) superó al Fondo B (${monto_b:.2f}).\n")
else:
    print(f"\nResultado final: El Fondo B (${monto_b:.2f}) superó al Fondo A (${monto_a:.2f}).\n")
