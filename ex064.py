n = 0
quantidade = 0
soma = 0
print('Os números digitados a seguir serão somados posteriormente e sua quantidade é de livre escolha.')
print('Para parar ou sair, digite "999"')
while n != 999:
    n = int(input('Digite um número inteiro: '))
    quantidade += 1
    soma += n
print('A soma dos {} números digitados é {}'.format(quantidade, soma - 999))
