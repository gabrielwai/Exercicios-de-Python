A1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
cont = 1
total = 0
termos = 10
continuar = 1
print('Os primeiros 10 termos dessa PA são: ')
while termos != 0:
    termos += cont
    while cont != termos:
        print('A{} = {}'.format(cont, A1 + (cont - 1) * r), end='')
        #print(A1 + (cont - 1) * r, end='')
        print(', ' if cont != 10 else '.', end='')
        cont += 1
    total = cont - 1
    termos = int(input('\nDeseja continuar com quantos termos?: '))
print('\nProgressão finalizada com {} termos mostrados.'.format(total))
