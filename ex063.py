print('-'*25)
print('Sequência de Fibonacci\n', end='-'*25)
n = int(input('\nQuantos números você quer mostrar?: '))
auxiliar = int
cont = 0
antecessor1 = -1 #antecessor imediatamente anterior
antecessor2 = 1
print('A sequência de Fibonacci dos {} primeiros termos são:'.format(n))
for cont in range(cont, n):
    print((antecessor1 + antecessor2)*-1, end='')
    print(' - ' if cont + 1 != n else '.', end='')
    auxiliar = antecessor1 + antecessor2
    antecessor2 = antecessor1
    antecessor1 = auxiliar
