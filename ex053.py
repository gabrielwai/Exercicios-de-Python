frase = str(input("Digite uma frase: "))
verificador = 0

frase = frase.split()
frase = ''.join(frase)
#print(frase)
for cont in range(0, len(frase)):
    if frase[cont] != frase[len(frase)-cont-1]:
        verificador = 1

if verificador == 0:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
