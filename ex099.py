from random import randint


def maior(*num):
    print('-=' * 30, end='\nAnalizando os valores passados...\n')
    for valores in range(len(num)):
        print(num[valores], end=' ')
    print()


numeros = list()
repetições = randint(1, 6)

for count in range(repetições):
    qtde = randint(1, 8)

    for c in range(qtde):
        numeros.append(randint(1, 10))
    maior(numeros)
    numeros.clear()
