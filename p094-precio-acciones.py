# p094-precio-acciones.py
# Análisis de precios de acciones diarias.
# Dada una lista de precios de cierre de una acción durante la semana.
# Encontrar el precio más alto, el más bajo y el día en que ocurrieron.

print("\033[2J\033[H", end="")

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
precios = [150.25, 152.30, 149.80, 151.00, 153.45, 154.10, 155.00]

precio_mas_alto = max(precios)
precio_mas_bajo = min(precios)
indice_mas_alto = precios. index(precio_mas_alto)
indice_mas_bajo = precios. index(precio_mas_bajo)

print("Análisis de precios de acciones:")
print(f"Precio mas alto: {precio_mas_alto} el día {dias[indice_mas_alto]}")
print(f"Precio más bajo: {precio_mas_bajo} el dia {dias[indice_mas_bajo]}")
