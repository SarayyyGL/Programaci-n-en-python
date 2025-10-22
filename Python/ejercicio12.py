entrada = input("Ingresa una secuencia de números separados por espacios: ")

numeros_str = entrada.split()

suma = 0
for num_str in numeros_str:
    suma += float(num_str)  

print("La suma total es:", suma)