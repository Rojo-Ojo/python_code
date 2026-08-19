# p017-convertir-temperatura.py
# Programa que convierte una temperatura de grados Celsius a grados Fahrenheit.

print("\033[2J\033[H", end="")
print("Programa que convierte una temperatura de grados Celsius a grados Fahrenheit.\n")

celcius = float(input("Grados Celcius: "))
print(f"\033[FGrados Celcius: {celcius}°C")
fahrenheit = (celcius * 9 / 5) + 32

print(f"\n{celcius:.2f}°C equivalen a {fahrenheit:.2f}°F\n")
