print('Preencha a tupla com 4 números.')
pos3 = 0
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('Você completou a túpla com os respectivos valores: ', end='| ')

for c in range(0, 4):
    print(núm[c], end=' | ')

if núm.count(9):
    print(f'\nO valor 9 apareceu {núm.count(9)} vezes')
else:
    print('\nO valor 9 não apareceu nenhuma vez')
if 3 in núm:
    print(f'O número 3 apareceu pela 1ª vez na {núm.index(3)+1}ª posição')
else:
    print('O número 3 não apareceu nenhuma vez')

print('Os números pares digitados foram: ', end='| ')
for c in range(0, 4):
    if núm[c] % 2 == 0:
        print(núm[c], end=' | ')
