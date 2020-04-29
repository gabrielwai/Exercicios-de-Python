lista = list()
ímpares = list()
pares = list()
print('Complete a lista numérica com 7 valores.')
for count in range(0, 7):
    lista.append(int(input('Digite um número inteiro: ')))
    if lista[count] % 2 != 0:
        ímpares.append(lista[count])
    else:
        pares.append(lista[count])
del lista
lista = list()
pares.sort()
ímpares.sort()
lista.append(pares[:])
lista.append(ímpares[:])
del ímpares
del pares
print(f'Os números pares digitados foram: {lista[0]}')
print(f'Os números ímpares digitados foram: {lista[1]}')
