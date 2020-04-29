núm = [[], []]
print('Preencha com 7 números inteiros.')
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 != 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[1]}')
print(f'Os valores ímpares digitados foram: {núm[0]}')
