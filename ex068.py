import random
cont = 0
print('=-' * 13, end='\nVAMOS JOGAR PAR OU ÍMPAR\n')
print('=-' * 13)
while True:
    n = int(input('Diga um valor (0 - 10): '))
    parOuImpar = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()

    parOuImpar = parOuImpar[0]
    nComputador = random.randint(0, 10)

    print('-'*26)
    print(f'Você jogou {n} e o computador {nComputador}. Total de {n + nComputador}. DEU ', end='')

    if (n + nComputador) % 2 == 0:
        print('PAR')
        print('-' * 26)
        if parOuImpar == 'P':
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
        else:
            print('Você PERDEU!\n', end='=-' * 13)
            print(f'\nGAME OVER! Você venceu {cont} vezes.\n')
            break
    else:
        print('ÍMPAR')
        print('-' * 26)
        if parOuImpar == 'I':
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
        else:
            print('Você PERDEU!\n', end='=-' * 13)
            print(f'\nGAME OVER! Você venceu {cont} vezes.\n')
            break
