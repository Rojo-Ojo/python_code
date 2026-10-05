# p103-resumen-ventas_v2.py
# Transforma una lista de ventas usando una función y compresión de listas
# La transformación aplica 3 pasos en una misma función,
# la función procesa la transformación, luego en el programa principal es llamada.
# Esta funcion aplica 3 transformaciones a cada elemento que le llega como parametro (una venta),
# regresa el resultado de la transformación.

def transformar_venta(venta):
    # Paso 1: si la venta es mayor o igual a 1000 aplica un descuento del 10%.
    if venta >= 1000:
        venta = venta * 0.9
    else:
    # Paso 2: si la venta es menor a 1000 aplica un descuento del 5%.
        venta = venta * 0.95
    return venta

print("\033c", end="")
print("\033[1;34m" + "Resumen de ventas v2." + "\033[0m\n")

# Ventas del mes (10) varias con decimales.
ventas = [1000, 2000, 3000, 400, 500, 1500.50, 800.75, 1200.25, 600.60, 2500.80]
ventast = [transformar_venta(venta) for venta in ventas]

print("Ventas originales:", ventas)
print("Ventas transformadas:", ventast)
