palavras = ('Trabalhar', 'python', 'alcançar', 'estudar', 'linguagem', 'pROGRaMADOr')
#vogais = ('A', 'E', 'I', 'O', 'U')
'''A variável c representa a letra e count a string/palavra da tupla'''

print('=-'*20, end='=\n')
print(f'{"CONTADOR DE VOGAIS":^41}')
print('=-'*20, end='=\n')

for count in range(0, len(palavras)):
    print(f'Na palavra {palavras[count].upper()} temos', end=' ')

    for c in range(0, len(palavras[count])):
        if 'A' in (palavras[count])[c].upper():
            print('a', end=' ')
        elif 'E' in (palavras[count])[c].upper():
            print('e', end=' ')
        elif 'I' in (palavras[count])[c].upper():
            print('i', end=' ')
        elif 'O' in (palavras[count])[c].upper():
            print('o', end=' ')
        elif 'U' in (palavras[count])[c].upper():
            print('u', end=' ')
    print()
