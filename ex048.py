print('A soma dos números ímpares múltiplos de 3 que estão no intervalo de 1 a 500 são:')
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        print(cont)