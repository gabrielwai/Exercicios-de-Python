n = int(input('Digite um número a saber seu fatorial: '))
fatorial = 1
c = n
print('O fatorial de {} = {}! ='.format(n, n), end=' ')
while c != 0:
    print(c, end='')
    print(' x ' if c != 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial)
