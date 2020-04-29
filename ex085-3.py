lista = list()
ímpares = list()
pares = list()
count = 0
lista.append(ímpares) # lista[0]
lista.append(pares) # lista[1]
print('Complete a lista numérica com 7 valores.')

while len(lista[0]) + len(lista[1]) != 7:
    print(f'count = {count}')
    lista[1].append(int(input('Digite um número inteiro: ')))
    print(lista)
    if lista[1][count] % 2 != 0:
        lista[0].append(lista[1][count])
        del lista[1][count]
        count -= 1
    count += 1
    print(lista)

pares.sort()
ímpares.sort()
lista.append(pares[:])
lista.append(ímpares[:])
del ímpares
del pares
print(f'Os números pares digitados foram: {lista[0]}')
print(f'Os números ímpares digitados foram: {lista[1]}')
