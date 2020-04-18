soma = 0  # somatório das idades para no final fazer a média
oldestman = str
mulheres_jovens = 0
menor = int
#menor = -1

for pessoa in range(1, 5):
    nome = str(input('Digite o nome da {} pessoa: '.format(pessoa)))
    idade = int(input('Digite a idade dessa pessoa: '))
    sexo = str(input('Digite por último o sexo da mesma pessoa (utilize "M" para masculino e "F" para feminino): '))

    #if menor == -1 and sexo == 'm':
    if pessoa == 1 and sexo == 'm':
        menor = idade
        oldestman = nome
    elif (idade > menor) and sexo in 'Mm':
        menor = idade
        oldestman = nome

    soma += idade

    if sexo in 'Ff' and idade < 20:
        mulheres_jovens += 1

print('A média das idades digitadas é {:.1f}\nO nome do homem mais velho é {}\nO número de mulheres menores de 20 anos de idade é {}.'.format(soma / 4, oldestman, mulheres_jovens))
