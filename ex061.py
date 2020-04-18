A1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
cont = 1
print('Os primeiros 10 termos dessa PA são: ')
while cont != 11:
    print('A{} = '.format(cont), end='')
    print(A1 + (cont - 1) * r, end='')
    print(', ' if cont != 10 else '.', end='')
    cont += 1
