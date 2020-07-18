nome = str(input('Digite seu nome completo: '))
nome = nome.lower()
#if nome.find('silva') >= 0:
if 'silva' in nome:
    print('Verdadeiro')
    #print(nome.find('silva'))
else:
    print('Falso')
