lista = list()
pares = list()
ímpares = list()
#continuar = ''

while True:
    continuar = ''
    lista.append(int(input('Digite um número inteiro: ')))

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        continuar = continuar[0]

        if continuar != 'S' and continuar != 'N':
            print('Valor inválido, tente novamente.')

    if continuar == 'N':
        break
    #elif continuar == 'S':
        #continuar = ''

for count in range(0, len(lista)):
    if lista[count] % 2 != 0:
        ímpares.append(lista[count])
    else:
        pares.append(lista[count])

print(f'A lista primeiro preenchida foi: {lista}\nOs números ímpares digitados foram: {ímpares}')
print(f'Já os números pares foram: {pares}')
