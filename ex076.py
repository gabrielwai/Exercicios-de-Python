listagem = ('Pão', 3.50, 'Leite', 4, 'Lápis', 1.75, 'Borraha', 2,
            'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3,
            'Livro', 34.9)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
#print('{:^40}'.format('LISTAGEM DE PREÇOS')) # <<< Também funciona assim
print('-'*40)

for count in range(0, len(listagem)):
    if count % 2 == 0:
        print(f'{listagem[count]:.<30}', end='')
    else:
        print(f'R${listagem[count]:>7.2f}')

print('-'*40)
