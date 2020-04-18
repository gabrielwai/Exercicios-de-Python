n = int
continuar = str
continuar = 's'
maior = int
menor = int
soma = float
soma = 0
quantidade = 1
n = int(input('Digite um número inteiro: '))
maior = n
menor = n
soma += n
continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
continuar = continuar[0]
while continuar != 'N' and continuar != 'S':
    continuar = str(input('Verifique novamente o valor recém digitado e tente novamente.\nDeseja continuar? [S/N]: ')).upper().strip()
    continuar = continuar[0]
while continuar == 'S':
    n = int(input('Digite um número: '))
    quantidade += 1
    soma += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    continuar = continuar[0]
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Verifique novamente o valor recém digitado e tente novamente.\nDeseja continuar? [S/N]: ')).upper().strip()
        continuar = continuar[0]
print(f'Programa finalizado com {quantidade} números digitados sendo sua média igual a {soma/quantidade:.2f}')
