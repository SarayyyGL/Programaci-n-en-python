n = int(input("Dime cuántos números vas a introducir: "))
print(f"Escribe {n} números:")

primero = int(input())
mayor = primero
menor = primero

for i in range(n - 1):
    num = int(input())
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print(f"El mayor es {mayor}")
print(f"El menor es {menor}")