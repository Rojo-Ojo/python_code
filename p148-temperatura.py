# p148-temperatura.py
# Permite elegir entre diferentes tipos de conversión de temperatura,
# las opciones estan en un menu y se puede elegir la opcion deseada
# C a F y F a C

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def celsius_a_fahrenheit(celsius:float) -> float:
    """ Convierte de Celsius a Fahrenheit """
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit:float) -> float:
    """ Convierte de Fahrenheit a Celsius """
    return (fahrenheit - 32) * 5/9

def main() -> None:
    """ Muestra el menu de opciones """
    while True:
        print("\nMenu de conversion de temperatura")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Salir")
        opcion = int(input("Elige una opcion (1-3): "))
        if opcion == 1:
            celsius = float(input("Dame la temperatura en Celsius: "))
            print(f"{celsius} C = {celsius_a_fahrenheit(celsius) } F")
        elif opcion == 2:
            fahrenheit = float(input("Dame la temperatura en Fahrenheit: "))
            print(f"{fahrenheit} F = {fahrenheit_a_celsius(fahrenheit)} C")
        elif opcion == 3:
            print("Saliendo del programa ... ")
            break
        else:
            print("Opcion invalida, intenta de nuevo.")

if __name__ == "__main__":
    main()
