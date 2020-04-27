expressão = str(input('Digite uma expressão matemática: '))

if expressão.count(')') == expressão.count('('):
    print('Expressão válida (referente aos parênteses)')
else:
    print('Expressão inválida, reveja os parênteses')
