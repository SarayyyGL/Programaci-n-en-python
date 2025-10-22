total = 0
while True:
    precio = float(input("Introduce un precio (0 para terminar): "))
    if precio == 0:
        break
    total += precio
print(f"El total de la factura es: {total:.2f}")