import random
numeros = (random.randint(0, 10), random.randint(0, 10),
           random.randint(0, 10), random.randint(0, 10),
           random.randint(0, 10))
menor = numeros[0]
maior = numeros[0]
for count in range(1, 5):
    if numeros[count] < menor:
        menor = numeros[count]
    if numeros[count] > maior:
        maior = numeros[count]
print('Os números sorteados foram: ', end='')
for n in range(0, 4):
    print(numeros[n], end=', ')
print(numeros[4], end='.')
print('\nO menor valor foi o {}.\nJá o maior valor foi {}.'.format(menor, maior)) #pode-se utilizar também das f-strings
