palavras = ('Trabalhar', 'python', 'alcançar', 'estudar', 'linguagem', 'programador')

print('=-'*20, end='=\n')
print(f'{"CONTADOR DE VOGAIS":^41}')
print('=-'*20, end='=')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
