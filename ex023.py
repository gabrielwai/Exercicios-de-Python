n = str(input('Digite um número entre 0 a 9999: '))

print('Unidades: {}'.format(n[(len(n))-1]))
if len(n) >= 2:
    print('Dezenas: {}'.format(n[(len(n))-2]))
else:
    print('Dezenas: 0')

if(len(n)) >= 3:
    print('Centenas: {}'.format(n[(len(n))-3]))
else:
    print('Centenas: 0')

if(len(n)) == 4:
    print('Milhares: {}'.format(n[(len(n))-4]))
else:
    print('Centenas: 0')