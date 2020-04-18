A1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
continuar = 1
cont = 1
total = 10
print('Os primeiros 10 termos dessa PA são: ')
while cont != 11:
    print('A{} = '.format(cont), end='')
    print(A1 + (cont - 1) * r, end='')
    print(', ' if cont != 10 else '.\n', end='')
    cont += 1
while continuar != 0:
    continuar = int(input('Deseja continuar com mais quantos termos?: '))
    if continuar != 0:
        total += continuar
        continuar += cont
    else:
        print('\nProgressão finalizada com {} termos mostrados.'.format(total))
    while continuar > cont:
        print('A{} = '.format(cont), end='')
        print(A1 + (cont - 1) * r, end='')
        print(', ' if cont + 1 < continuar else '.\n', end='')
        cont += 1
