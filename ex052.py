from math import floor

n = int(input('Digite um número: '))
verificador = 0

for cont in range(2, floor(n/2)+1):
    if n % cont == 0:
        verificador = 1
        print("Quantas vezes rodou {}".format(cont))
        break
        #cont = n

if verificador == 0 and n != 1 and n != 0:
    print('O número digitado é primo.')
else:
    print('O número digitado não é primo.')
