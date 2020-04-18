A1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
for n in range(1, 11):
    print('A{} = {}'.format(n, A1+(n-1)*r) )
