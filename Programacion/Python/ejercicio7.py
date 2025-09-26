nota = float(input("Introduce una nota (0–10): "))

if nota < 0 or nota > 10:
    print("Nota no válida")
else:
    if nota < 5:
        print("Insuficiente")
    elif nota < 6:
        print("Suficiente")
    elif nota < 7:
        print("Bien")
    elif nota < 9:  # Notable: 7 ≤ n < 9
        print("Notable")
    else:  # Sobresaliente: 9 ≤ n ≤ 10
        print("Sobresaliente")