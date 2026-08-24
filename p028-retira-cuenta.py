# p028-retira-cuenta.py
# Simula el retiro de dinero de una cuenta con validación.

print("\033[2J\033[H", end="")
print("Simula el retiro de dinero de una cuenta con validación.\n")

saldo_cuenta = 1500.00
cantidad_retiro = float(input(f"Cantidad a retirar de la cuenta con saldo ${saldo_cuenta}\nRetiro: "))
print(f"\033[FRetiro: ${cantidad_retiro}")

if cantidad_retiro > 0:
    print("\nProcedemos al retiro...")
    if cantidad_retiro <= saldo_cuenta:
        nuevo_saldo = saldo_cuenta - cantidad_retiro
        print(f"\nRetiro Exitoso, tu nuevo saldo es: ${nuevo_saldo}")
    else:
        print(f"\nQuieres retirar ${cantidad_retiro} pero tienes ${saldo_cuenta}, operación fallida.")
else:
    print("\nLa cantidad a retirar debe ser un número positivo.")

print("\nGracias por usar nuestro servicio.")
