# p136-segundo-examen-parcial.py
# AeroRegistro: captura, procesamiento e impresión del registro de vuelos.

# ============================================================
# 1. CAPTURA DE DATOS
# ============================================================

vuelos = []  # Lista de diccionarios, uno por vuelo

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

print("=== AeroRegistro ===")
print("Para terminar, deje vacío el número de vuelo o escriba '*'.\n")

while True:
    numero_vuelo = input("Número de vuelo (ej. AA-101): ").strip()

    # Condición de salida: cadena vacía o "*"
    if numero_vuelo == "" or numero_vuelo == "*":
        break

    origen = input("Origen: ").strip()
    destino = input("Destino: ").strip()
    aerolinea = input("Aerolínea: ").strip()

    # Pasajeros: se repite la lectura hasta recibir un entero >= 0
    while True:
        try:
            pasajeros = int(input("Pasajeros a bordo: "))
            if pasajeros >= 0:
                break
            print("Error: el valor no puede ser negativo.")
        except ValueError:
            print("Error: ingrese un número entero válido.")

    # Tarifa: se repite la lectura hasta recibir un real > 0
    while True:
        try:
            tarifa = float(input("Tarifa del boleto (MXN): "))
            if tarifa > 0:
                break
            print("Error: la tarifa debe ser mayor que cero.")
        except ValueError:
            print("Error: ingrese un número válido (ej. 2350.75).")

    # Se guarda el vuelo como diccionario dentro de la lista general
    vuelos.append({
        "numero_vuelo": numero_vuelo,
        "origen": origen,
        "destino": destino,
        "aerolinea": aerolinea,
        "pasajeros": pasajeros,
        "tarifa": tarifa,
    })
    print("Vuelo registrado.\n")

# ============================================================
# 2. DESTINOS ÚNICOS Y REGISTRO INMUTABLE
# ============================================================

destinos_unicos = set()   # El conjunto descarta destinos repetidos
registro_inmutable = []   # Lista de tuplas (numero_vuelo, aerolinea, destino)

for vuelo in vuelos:
    destinos_unicos.add(vuelo["destino"])
    registro_inmutable.append(
        (vuelo["numero_vuelo"], vuelo["aerolinea"], vuelo["destino"])
    )

# ============================================================
# 3. IMPRESIÓN DE DATOS
# ============================================================

print("\n\nDatos (Lista de diccionarios):\n", vuelos)
print("\nDestinos Únicos (Conjunto):\n", destinos_unicos)
print("\nRegistro Inmutable (Tuplas):\n", registro_inmutable)

# Tabla: anchos fijos (12 + 20 + 20 + 15 + 10 + 12 = 89 caracteres)
# "<" alinea a la izquierda (texto) y ">" a la derecha (números)
print()
print(f"{'No. Vuelo':<12}{'Origen':<20}{'Destino':<20}"
      f"{'Aerolínea':<15}{'Pasajeros':>10}{'Tarifa':>12}")
print("-" * 89)

for vuelo in vuelos:
    print(
        f"{vuelo['numero_vuelo']:<12}"
        f"{vuelo['origen']:<20}"
        f"{vuelo['destino']:<20}"
        f"{vuelo['aerolinea']:<15}"
        f"{vuelo['pasajeros']:>10}"
        f"{vuelo['tarifa']:>12.2f}"
    )

# ============================================================
# 4. CÁLCULOS DEL RESUMEN
# ============================================================

total_vuelos = len(vuelos)
conteo_aerolineas = {}  # {aerolínea: cantidad de vuelos}
conteo_destinos = {}    # {destino: cantidad de vuelos}
suma_pasajeros = 0
suma_tarifas = 0.0
tarifa_maxima = None    # Mayor tarifa encontrada
tarifa_minima = None    # Menor tarifa encontrada
vuelos_caros = []       # Números de vuelo con la tarifa máxima
vuelos_baratos = []     # Números de vuelo con la tarifa mínima

# Un solo recorrido acumula conteos, sumas y extremos
for vuelo in vuelos:
    # .get(clave, 0) devuelve 0 si la clave aún no existe
    conteo_aerolineas[vuelo["aerolinea"]] = conteo_aerolineas.get(vuelo["aerolinea"], 0) + 1
    conteo_destinos[vuelo["destino"]] = conteo_destinos.get(vuelo["destino"], 0) + 1

    suma_pasajeros += vuelo["pasajeros"]
    suma_tarifas += vuelo["tarifa"]

    # Comparaciones estrictas: en caso de empate se conservan los vuelos detectados.
    if tarifa_maxima is None or vuelo["tarifa"] > tarifa_maxima:
        tarifa_maxima = vuelo["tarifa"]
        vuelos_caros = [vuelo["numero_vuelo"]]
    elif vuelo["tarifa"] == tarifa_maxima:
        vuelos_caros.append(vuelo["numero_vuelo"])

    # Misma lógica para la tarifa mínima
    if tarifa_minima is None or vuelo["tarifa"] < tarifa_minima:
        tarifa_minima = vuelo["tarifa"]
        vuelos_baratos = [vuelo["numero_vuelo"]]
    elif vuelo["tarifa"] == tarifa_minima:
        vuelos_baratos.append(vuelo["numero_vuelo"])

# ============================================================
# 5. IMPRESIÓN DEL RESUMEN
# ============================================================

print("\nResumen:")
print(f"\nVuelos totales: {total_vuelos}")

print("\nAerolíneas:")
for nombre, cantidad in conteo_aerolineas.items():
    print(f"• {nombre}: {cantidad}")

print("\nDestinos:")
for nombre, cantidad in conteo_destinos.items():
    print(f"• {nombre}: {cantidad}")

# Los promedios solo se calculan si hay vuelos (evita dividir entre cero)
if total_vuelos > 0:
    promedio_pasajeros = suma_pasajeros / total_vuelos
    promedio_tarifa = suma_tarifas / total_vuelos

    # ":,.2f" = separador de miles y dos decimales
    print(f"\nPasajeros -> Suma: {suma_pasajeros}, Promedio: {promedio_pasajeros:,.2f}")
    print(f"Tarifa -> Suma: {suma_tarifas:,.2f}, Promedio: {promedio_tarifa:,.2f}")
        # Singular si hay un solo vuelo; plural si hay empate
    if len(vuelos_caros) == 1:
        texto_caro = f"{vuelos_caros[0]} de ${tarifa_maxima:,.2f} es el más caro"
    else:
        texto_caro = f"{', '.join(vuelos_caros)} de ${tarifa_maxima:,.2f} son los más caros"

    if len(vuelos_baratos) == 1:
        texto_barato = f"{vuelos_baratos[0]} de ${tarifa_minima:,.2f} es el más barato"
    else:
        texto_barato = f"{', '.join(vuelos_baratos)} de ${tarifa_minima:,.2f} son los más baratos"

    print(f"{texto_caro}, {texto_barato}.")
else:
    print("No se registraron vuelos, no hay cálculos que mostrar.")