'''from time import sleep

print('Testando...', end= '')
sleep(1.3)
print('\nAgora sim, Finalizando.')'''

import random

lista = list()
ordenados = list()
for i in range(0, 5):
    lista.append(random.randint(1, 10))
for i in lista:
    print(f' {i},', end='')

i = 0
f = 1
ordenados.append(lista[0])
while i <= len(lista):
    if lista[i+1] < ordenados[0]:
        for c in range(0, ):
            ordenados[f] = ordenados[f-1]
