print('-'*96, end='\n')
print('\t'*10, end='AMG Produtos\n')
print('-'*96)
nomemaisbarato = ''
mais_de_1000 = 0
total = 0
maisbarato = -1
continuar = 'S'

while True:
    if continuar == 'N':
        break
    produto = str(input('Nome do produto: ')).strip().title()
    preço = -1
    while preço < 0:
        preço = float(input('Preço do produto: R$'))
        if preço < 0:
            print('Preço deve ser positivo, verifique o valor inserido e tente novamente.')

    total += preço
    if preço > 1000:
        mais_de_1000 += 1

    if maisbarato == -1:
        maisbarato = preço
        nomemaisbarato = produto
    elif preço < maisbarato:
            maisbarato = preço
            nomemaisbarato = produto

    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
        continuar = continuar[0]
        if continuar == 'N':
            print('\nFinalizando o Programa...\n')
            break
        if continuar != 'S':
            print('Valor inválido. Tente novamente.')

print(f'O produto mais barato é o/a {nomemaisbarato} que custa R${maisbarato:.2f}')
print(f'A quantidade de produtos cadastrados valendo mais de R$1000 é {mais_de_1000}')
print(f'O total foi de R${total:.2f}')
