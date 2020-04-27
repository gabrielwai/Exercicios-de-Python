expressão = str(input('Digite uma expressão matemática: '))

if expressão.count(')') == expressão.count('('):
    print('Expressão válida (referente aos parênteses)')
else:
    print('Expressão inválida, reveja os parênteses')
# ERRADO! Basta tentar o seguinte input: 6 + ) 85 (
# Deta forma não é possível detectar a hierarquicidade dos parênteses
