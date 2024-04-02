
# Ejercicio 1 Solicitar al usuario que ingrese su nombre
nombre_usuario = input("Por favor, ingresa tu nombre: ")

# Mostrar un saludo personalizado
print(f"¡Hola {nombre_usuario}!")


# Ejercicio 2 - Solicitar al usuario dos números enteros

n = int(input("Ingrese el primer número entero: "))
m = int(input("Ingrese el segundo número entero: "))

# Calcular el cociente y el resto de la división entera
c = n // m  # Cociente
r = n % m   # Resto
# Mostrar el resultado por pantalla
print(f"{n} entre {m} da un cociente {c} y un resto {r}.")

# Ejercicio 3 solicitar al usuario la cantidad a invertir, el interés anual y el número de años.

cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (%): "))
num_anios = int(input("Ingrese el número de años: "))

# Calcular el capital obtenido en la inversión
capital_obtenido = cantidad_invertir * (1 + (interes_anual / 100)) ** num_anios

# Mostrar el capital obtenido por pantalla
print(f"El capital obtenido después de {num_anios} años será de: {capital_obtenido:.2f}")

# Ejercicio 4 Definir el peso de los payasos y muñecas

peso_payaso = 112  # en gramos
peso_muneca = 75   # en gramos

# Leer el número de payasos y muñecas vendidos en el último pedido
num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_munecas = int(input("Ingrese el número de muñecas vendidas: "))

# Calcular el peso total del paquete
peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

# Mostrar el peso total del paquete
print(f"El peso total del paquete que será enviado es de {peso_total} gramos.")

# Ejercicio 5 Leer la cantidad de dinero depositada en la cuenta de ahorros
cantidad_depositada = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))

# Calcular el saldo después del primer año
saldo_despues_1_anio = cantidad_depositada * (1 + 0.04)

# Calcular el saldo después del segundo año
saldo_despues_2_anios = saldo_despues_1_anio * (1 + 0.04)

# Calcular el saldo después del tercer año
saldo_despues_3_anios = saldo_despues_2_anios * (1 + 0.04)

# Mostrar los saldos después de cada año
print(f"Saldo después del primer año: {saldo_despues_1_anio:.2f}")
print(f"Saldo después del segundo año: {saldo_despues_2_anios:.2f}")
print(f"Saldo después del tercer año: {saldo_despues_3_anios:.2f}")

#Ejercicio 6 - Definir el precio de una barra de pan y el descuento por no ser fresca 
precio_barra_pan = 3.49  # en euros
descuento_no_fresca = 0.60  # 60%

# Leer el número de barras vendidas que no son del día
num_barras_no_frescas = int(input("Ingrese el número de barras vendidas que no son del día: "))

# Calcular el precio habitual de una barra de pan
precio_habitual = precio_barra_pan

# Calcular el descuento aplicado por no ser fresca
descuento = precio_barra_pan * descuento_no_fresca

# Calcular el coste final total
coste_final_total = (precio_barra_pan - descuento) * num_barras_no_frescas

# Mostrar los resultados por pantalla
print(f"Precio habitual de una barra de pan: {precio_habitual:.2f} euros")
print(f"Descuento por no ser fresca: {descuento:.2f} euros")
print(f"Coste final total: {coste_final_total:.2f} euros")

