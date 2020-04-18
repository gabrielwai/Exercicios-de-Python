n = -1
while n < 0:
    n = int(input('Digite um número a saber seu fatorial: '))
    if n < 0:
        print('Valores negativos não são permitidos. Tente novamente.')
    else:
        if n == 0:
            print('O fatorial de {} é igual a 1'.format(n))
        else:
            fatorial = n
            print('O fatorial de {} = {}! ='.format(n, n), end=' ')
            for contador in range(n, 1, -1):
                print(contador, end=' x ')
            if n != 1:
                print('1', end=' = ')
            contador = 1
            while contador != n:
                fatorial *= (n-contador)
                contador += 1
            print(fatorial)
