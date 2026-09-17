# p081-plan-ahorro-depositos-mensuales.py
# Programa que simula un plan de ahorro, solicita al usuario un monto inicial, un depósito mensual fijo, una tasa de interés mensual (porcentaje),
# y el número total de meses del plan. El programa muestra una tabla que detalle, para cada mes, el saldo inicial, el interés ganado en ese mes, 
# y el saldo final. El interés se calcula sobre el saldo inicial antes de sumar el nuevo depósito.

print("\033[2J\033[H", end="")
print("Programa que simula un plan de ahorro, solicita al usuario un monto inicial, un depósito mensual fijo, una tasa de interés mensual (porcentaje),\n"
      "y el número total de meses del plan. El programa muestra una tabla que detalle, para cada mes, el saldo inicial, el interés ganado en ese mes,\n" 
      "y el saldo final. El interés se calcula sobre el saldo inicial antes de sumar el nuevo depósito.\n")

monto = float(input("Monto inicial de ahorro: "))
deposito = float(input("Depósito mensual: "))
interes = float(input("Tasa de interés mensual (%): "))
meses = int(input("Número de meses a simular: "))

print("\n-- Plan de Ahorro Detallado --")

for i in range(1, meses+1):
    print(f"Mes {i}: Saldo Inicial: ${monto:<5.2f} | Interés: ${monto * (interes/100):<5.2f} | Saldo Final: ${monto + deposito + monto * (interes/100):<10.2f}")
    monto += deposito + monto * (interes/100)

print(f"\nAl final de {meses} meses, tendrás ${monto:.2f}\n")
