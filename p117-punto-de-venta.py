# p117-punto-de-venta.py
# Crear un sistema simple de punto de venta (POS) para un puesto de comida.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

comida = {
    "Hamburguesa": 5.0,
    "Papas Fritas": 2.5,
    "Refresco": 1.5,
    "Hot Dog": 3.0,
    "Pizza": 8.0
}

# Mostrar Menú: Mostrar al usuario los productos disponibles y sus precios, iterando sobre el diccionario.
print("Menú de productos:")
for producto, precio in comida.items():
    print(f"- {producto}: ${precio :.2f}")

# Tomar Orden: Preguntar al usuario qué desea ordenar en un bucle.
orden = {}
while True:
    producto = input("Ingrese el producto que desea ordenar (o presione <Enter> para finalizar): ")
    if producto == "":
        break
    if producto not in comida:
        print("Producto no disponible. Intente nuevamente.")
        continue
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    if producto in orden:
        orden [producto] += cantidad
    else:
        orden [producto] = cantidad

# Mostrar un recibo con el subtotal por producto y el total general de la compra.
print("\nRecibo de compra:")
total_general = 0
for producto, cantidad in orden.items():
    subtotal = comida [producto] * cantidad
    total_general += subtotal
    print(f"- {producto} x {cantidad} : ${subtotal :.2f}")
print(f"Total general: ${total_general :.2f}")
