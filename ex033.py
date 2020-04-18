n1 = int(input('Digite um número inteiro qualquer: '))
n2 = int(input('Digite um outro número inteiro qualquer: '))
n3 = int(input('Digite outro número inteiro qualquer: '))

if n1 > n2:
    if n1 > n3:
        maior = n1
        if n2 > n3:
            menor = n3
        else:
            menor = n2
    else:
        maior = n3
        menor = n2
else:
    if n2 > n3:
        maior = n2
        if n1 > n3:
            menor = n3
        else:




