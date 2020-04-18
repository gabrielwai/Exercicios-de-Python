lista = list()
print('Digite 5 números inteiros.')

lista.append(int(input('Digite um valor inteiro: ')))
maior = lista[0]
print('Valor adicionado na última posição do lista.')

for count in range(1, 5):
    lista.append(int(input('Digite um valor inteiro: ')))

    for c in range(0, count):
        if lista[count] < lista[c]:
            lista.insert(c, lista[count])
            lista.pop()
            print(f'Valor inserido no índice {c}')
            break

        if lista[count] > maior:
            maior = lista[count]
            print('Valor adicionado na última posição do lista.')

print(f'Os valores digitados em ordem são: {lista}')
