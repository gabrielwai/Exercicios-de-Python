def área(l, c):
    print(f'A área de um terreno de {l}x{c} é de {c*l}m².')


print('Controle de Terrenos\n', end='-'*len('Controle de Terrenos'))
largura = float(input('\nLARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)
