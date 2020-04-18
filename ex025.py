nome = str(input('Digite seu nome completo: '))
nome = nome.lower()
if nome.find('silva') >= 0:
    print('Verdadeiro')
else:
    print('Falso')