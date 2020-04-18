listagem = ('Pão', 3.50, 'Leite', 4, 'Lápis', 1.75, 'Borraha', 2,
            'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3,
            'Livro', 34.9)
print('-'*65)
print('{:^66}'.format('LISTAGEM DE PREÇOS')) # alinhamento de texto
print('-'*65)
maior = 0
espaços = 0
multiplicador = 10
teste = 6
# -----------------------------------------------------------------------
# Encontra o maior preço da lista e coloca na variável 'maior':
for count in range(0, len(listagem)):
    if count % 2 == 1 and listagem[count] > maior:
        maior = listagem[count]
count = 10
# -----------------------------------------------------------------------
#print(maior)
# -----------------------------------------------------------------------
# Interpreta a quantidade de dígitos em 'maior'; ex: 'maior' == 213.79 então 'maior' = 100.00
while True:
    if maior >= count:
        count *= 10
    else:
        count /= 10
        maior = count
        break
#print(maior)
# -----------------------------------------------------------------------
count = 10
# -----------------------------------------------------------------------
# Conta quantos espaços o preço deve ter no output de acordo com o valor obtido em 'maior'
while maior / count > 0:
    if maior == count:
        espaços += 1
        break
    else:
        espaços += 1
        count *= 10
espaços *= 3
# -----------------------------------------------------------------------
#print(espaços)
count = 0
# 100.00 -> 6
while count < len(listagem):
    if count % 2 == 0:
        print(listagem[count], end='')
        print('.'*(54-(len(listagem[count]))), end='') # Quantidade de pontos para cada produto
    else:
        print('R$ ', end='')
        print('{:>6.2f}'.format(listagem[count]))
    count += 1

print('-'*65)
