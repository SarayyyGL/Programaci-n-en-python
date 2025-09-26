#Notas.py
nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))

mayores_que_4 = 0
if nota1 > 4:
    mayores_que_4 += 1
if nota2 > 4:
    mayores_que_4 += 1
if nota3 > 4:
    mayores_que_4 += 1

if mayores_que_4 == 0:
    nota_final = 0
elif mayores_que_4 < 3:  # es decir, 1 o 2 notas > 4
    nota_final = 2
else:  # todas las notas son mayores que 4
    nota_final = 0.3 * nota1 + 0.2 * nota2 + 0.5 * nota3

print(f"La nota final es: {nota_final}")