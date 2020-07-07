nome = str(input('Digite seu nome completo: '))

print("Seu nome todo em maiúsculo é: {}".format(nome.upper()))
print("\nSeu nome todo em minúsculo é: {}".format(nome.lower()))
print("Qtdd de espaços totais: {}".format(nome.count(' ')))
print('Total de letras (desconsiderando os espaços): {}'.format(len(nome)-nome.count(" ")))
print('Primeiro nome: {}'.format(nome[:nome.find(' ')]))
print('Quantidade de letras que possui o primeiro nome: {}'.format(len(nome[:nome.find(' ')])))
#nome teste: Wirllbda Olnd  Silva NkbsKj
