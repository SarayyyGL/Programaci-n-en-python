print('Dame el numero de chicos de la clase')
chicos=int(input())
print('Dame el numeoro de chicas de la clase')
chicas=int(input())

total = chicos+chicas
pchicas=(chicas/total)*100
pchicos=(chicos/total)*100

print('RESUMEN')
print(f'EL número total de alumnos {total}')

print(f'El porcentaje de las chicas es de {pchicas:.2f}%')
print(f'El porcentaje de los chicos es de {pchicos:.2f}%')