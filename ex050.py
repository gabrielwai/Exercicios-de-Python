soma = 0
n = int(input('Digite um número inteiro: '))
if(n%2==0):
    soma += n
for cont in range(0, 6):
    n = int(input('Digite novamente um número inteiro: '))
    if n%2==0:
        soma += n
print('A soma dos números pares digitados é igual a {}'.format(soma))
