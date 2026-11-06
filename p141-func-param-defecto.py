# p141-func-param-defecto.py
# Uso de parámetros con valores por defecto.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def calcular_total(monto:float, iva:float=0.16) -> float:
    return monto + (monto * iva)

print(f'El total a pagar es: {calcular_total (1000) :,.2f}')
print(f'El total a pagar es: {calcular_total(1000, 0.10):,.2f}')
