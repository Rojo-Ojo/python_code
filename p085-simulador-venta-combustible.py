# ================================================
# Sistema Integral de Gasolinera
# ================================================

opcion_texto: str = ""   # str: texto crudo ingresado por el usuario
opcion: int = 0           # int: opción numérica del menú

while True:
    print("\n" + "=" * 42)
    print(f"{'MENÚ PRINCIPAL - GASOLINERA':^42}")
    print("=" * 42)
    print(f"{'1.':<4}{'Venta de Combustible':<38}")
    print(f"{'2.':<4}{'Simulación de Rendimiento':<38}")
    print(f"{'3.':<4}{'Clasificador de Cliente':<38}")
    print(f"{'4.':<4}{'Salir':<38}")
    print("=" * 42)

    opcion_texto = input("Seleccione una opción (1-4): ")

    try:
        opcion = int(opcion_texto)
    except ValueError:
        print(f"\n{'Error:':<10}'{opcion_texto}' no es una opción numérica válida.")
        continue

    # ------------------------------------------------
    # OPCIÓN 1: VENTA DE COMBUSTIBLE
    # ------------------------------------------------
    if opcion == 1:
        sub_opcion_texto: str = ""
        sub_opcion: int = 0
        tipo_combustible: str = ""
        precio_litro: float = 0.0
        litros: float = 0.0

        # --- Submenú de combustible (misma estructura que el menú principal) ---
        while True:
            print("\n" + "-" * 42)
            print(f"{'SELECCIÓN DE COMBUSTIBLE':^42}")
            print("-" * 42)
            print(f"{'1.':<4}{'Magna':<38}")
            print(f"{'2.':<4}{'Premium':<38}")
            print(f"{'3.':<4}{'Diésel':<38}")
            print("-" * 42)

            sub_opcion_texto = input("Seleccione el tipo de combustible (1-3): ")

            try:
                sub_opcion = int(sub_opcion_texto)
            except ValueError:
                print(f"{'Error:':<10}'{sub_opcion_texto}' no es una opción válida.\n")
                continue

            if sub_opcion == 1:
                tipo_combustible = "Magna"
            elif sub_opcion == 2:
                tipo_combustible = "Premium"
            elif sub_opcion == 3:
                tipo_combustible = "Diésel"
            else:
                print(f"{'Error:':<10}opción '{sub_opcion}' no válida. Elija entre 1 y 3.\n")
                continue

            break

        # --- Precio por litro (dato funcional, ingresado por el usuario) ---
        while True:
            entrada_precio = input(f"\nPrecio por litro de {tipo_combustible}: $")
            try:
                precio_litro = float(entrada_precio)
            except ValueError:
                print(f"{'Error:':<10}'{entrada_precio}' no es un número válido.\n")
                continue
            if precio_litro <= 0:
                print(f"{'Error:':<10}el precio debe ser mayor que cero.\n")
                continue
            break

        while True:
            entrada_litros = input(f"\nLitros de {tipo_combustible} a cargar: ")
            try:
                litros = float(entrada_litros)
            except ValueError:
                print(f"{'Error:':<10}'{entrada_litros}' no es un número válido.\n")
                continue
            if litros <= 0:
                print(f"{'Error:':<10}la cantidad debe ser mayor que cero.\n")
                continue
            break

        total: float = precio_litro * litros

        # División entera (//) y residuo (%): desglose de pago sugerido
        total_entero: int = int(total)
        billetes_1000: int = total_entero // 1000
        resto_0: int = total_entero % 1000
        billetes_500: int = resto_0 // 500
        resto_1: int = resto_0 % 500
        billetes_200: int = resto_1 // 200
        resto_2: int = resto_1 % 200
        billetes_50: int = resto_2 // 50
        resto_3: int = resto_2 % 50
        monedas_10: int = resto_3 // 10
        centavos_sueltos: int = resto_3 % 10

        print("\n" + "=" * 42)
        print(f"{'TICKET DE VENTA':^42}")
        print("=" * 42)
        print(f"{'Producto':<18}{'Litros':>10}{'Precio/L':>14}")
        print("-" * 42)
        print(f"{tipo_combustible:<18}{litros:>10.2f}{'$' + f'{precio_litro:.2f}':>14}")
        print("-" * 42)
        print(f"{'TOTAL A PAGAR:':<20}{'$' + f'{total:.2f}':>22}")
        print("=" * 42)
        print(f"{'Sugerencia de pago':^42}")
        print("-" * 42)
        print(f"{'Billetes de $1000:':<28}{billetes_1000:>10}")
        print(f"{'Billetes de $500:':<28}{billetes_500:>10}")
        print(f"{'Billetes de $200:':<28}{billetes_200:>10}")
        print(f"{'Billetes de $50:':<28}{billetes_50:>10}")
        print(f"{'Monedas de $10:':<28}{monedas_10:>10}")
        print(f"{'Resto (< $10):':<28}${centavos_sueltos:>9}")

    # ------------------------------------------------
    # OPCIÓN 2: SIMULACIÓN DE RENDIMIENTO
    # ------------------------------------------------
    elif opcion == 2:
        km_inicial: float = 0.0
        rendimiento: float = 0.0
        km_mensual: float = 0.0
        meses: int = 0

        while True:
            entrada_km = input("\nKilometraje inicial del vehículo: ")
            try:
                km_inicial = float(entrada_km)
            except ValueError:
                print(f"{'Error:':<10}'{entrada_km}' no es un número válido.\n")
                continue
            if km_inicial < 0:
                print(f"{'Error:':<10}el kilometraje no puede ser negativo.\n")
                continue
            break

        while True:
            entrada_rend = input("Rendimiento constante (km por litro): ")
            try:
                rendimiento = float(entrada_rend)
            except ValueError:
                print(f"{'Error:':<10}'{entrada_rend}' no es un número válido.\n")
                continue
            if rendimiento <= 0:
                print(f"{'Error:':<10}el rendimiento debe ser mayor que cero.\n")
                continue
            break

        while True:
            entrada_kmm = input("Kilometraje promedio recorrido por mes: ")
            try:
                km_mensual = float(entrada_kmm)
            except ValueError:
                print(f"{'Error:':<10}'{entrada_kmm}' no es un número válido.\n")
                continue
            if km_mensual <= 0:
                print(f"{'Error:':<10}el kilometraje mensual debe ser mayor que cero.\n")
                continue
            break

        while True:
            entrada_meses = input("Número de meses a proyectar: ")
            try:
                meses = int(entrada_meses)
            except ValueError:
                print(f"{'Error:':<10}'{entrada_meses}' no es un número entero válido.\n")
                continue
            if meses <= 0:
                print(f"{'Error:':<10}el número de meses debe ser mayor que cero.\n")
                continue
            break

        # Potencia (**): desgaste estimado del vehículo, proporcional al
        # cuadrado del kilometraje acumulado (crece más rápido con el uso)
        factor_desgaste: float = 0.00000002

        print("\n" + "-" * 66)
        print(f"{'PROYECCIÓN DE RENDIMIENTO':^66}")
        print("-" * 66)
        print(
            f"{'Mes':<6}{'Km acumulados':>15}{'Litros consumidos':>19}"
            f"{'Cambios aceite':>16}{'Desgaste':>10}"
        )
        print("-" * 66)

        for mes in range(1, meses + 1):
            km_recorridos: float = km_mensual * mes
            km_acumulados: float = km_inicial + km_recorridos
            litros_consumidos: float = km_recorridos / rendimiento

            # División entera (//): cada 5,000 km corresponde a un cambio de aceite
            cambios_aceite: int = int(km_acumulados) // 5000

            # Potencia (**): desgaste estimado (crece cuadráticamente con el uso)
            desgaste_pct: float = (km_acumulados ** 2) * factor_desgaste

            print(
                f"{mes:<6}{km_acumulados:>15.2f}{litros_consumidos:>19.2f}"
                f"{cambios_aceite:>16}{desgaste_pct:>9.2f}%"
            )

        print("-" * 66)

    # ------------------------------------------------
    # OPCIÓN 3: CLASIFICADOR DE CLIENTE
    # ------------------------------------------------
    elif opcion == 3:
        volumen_mensual: float = 0.0

        while True:
            entrada_vol = input("\nVolumen de compra mensual del cliente (L): ")
            try:
                volumen_mensual = float(entrada_vol)
            except ValueError:
                print(f"{'Error:':<10}'{entrada_vol}' no es un número válido.\n")
                continue
            if volumen_mensual <= 0:
                print(f"{'Error:':<10}el volumen debe ser mayor que cero.\n")
                continue
            break

        categoria: str = ""

        if volumen_mensual < 100:
            categoria = "Regular"
        elif volumen_mensual >= 100 and volumen_mensual <= 500:
            categoria = "Premium"
        else:
            categoria = "Flotilla"

        print("\n" + "-" * 42)
        print(f"{'CLASIFICACIÓN DE CLIENTE':^42}")
        print("-" * 42)
        print(f"{'Volumen mensual:':<20}{volumen_mensual:>18.2f} L")
        print(f"{'Categoría:':<20}{categoria:>21}")
        print("-" * 42)

    # ------------------------------------------------
    # OPCIÓN 4: SALIR
    # ------------------------------------------------
    elif opcion == 4:
        print(f"\n{'Gracias por usar el sistema. ¡Hasta pronto!':^42}")
        break

    # ------------------------------------------------
    # OPCIÓN INVÁLIDA
    # ------------------------------------------------
    else:
        print(f"\n{'Error:':<10}opción '{opcion}' no válida. Elija entre 1 y 4.")
        continue