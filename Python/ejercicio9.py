numero_secreto = 7

print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 10. ¿Puedes adivinarlo?")

adivinado = False
while not adivinado:
    intento = int(input("Ingresa tu intento: "))
    
    if intento == numero_secreto:
        print("¡Correcto! ¡Has adivinado el número!")
        adivinado = True  # Termina el bucle
    else:
        if intento > numero_secreto:
            print("Muy alto.")
        else:
            print("Muy bajo.")