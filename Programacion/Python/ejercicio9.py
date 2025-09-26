numero_secreto = 7

# Mensaje de bienvenida
print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 10. ¿Puedes adivinarlo?")

# Bucle while para permitir múltiples intentos
adivinado = False
while not adivinado:
    # Pedir al usuario que ingrese un número
    intento = int(input("Ingresa tu intento: "))
    
    # Condicionales anidados para dar pistas
    if intento == numero_secreto:
        print("¡Correcto! ¡Has adivinado el número!")
        adivinado = True  # Termina el bucle
    else:
        if intento > numero_secreto:
            print("Muy alto.")
        else:
            print("Muy bajo.")