lista = list()
linha = list()
coluna = list()
soma_pares = 0
soma_terceira_coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        coluna.append(int(input(f'Digite um número inteiro para [{l}, {c}]: ')))
    lista.append(coluna[:])
    coluna.clear()
print(lista)

print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {lista[l][c]} ]', end='')

        if lista[l][c] % 2 == 0:
            soma_pares += lista[l][c]

        if c == 2:
            soma_terceira_coluna += lista[l][c]
            print()

        if l == 1:
            if l == 1 and c == 0:
                maior_segunda_linha = lista[l][c]
            if maior_segunda_linha < lista[l][c]:
                maior_segunda_linha = lista[l][c]
print('-='*20)

print(f'A soma dos números pares digitados é: {soma_pares}')
print(f'A soma dos números da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')
