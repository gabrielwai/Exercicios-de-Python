menor = float
maior = float

for cont in range(0, 5):
    peso = float(input('Digite um peso (em Kg): '))

    if cont == 0:
        menor = peso
        maior = peso

    if peso < menor:
        menor = peso

    elif peso > maior:
        maior = peso

print('O maior peso digitado foi: {:.2f}Kg'.format(maior))
print('O menor peso digitado foi: {:.2f}Kg'.format(menor))
