lista = list()
linha = list()
coluna = list()
for l in range(0, 3):
    for c in range(0, 3):
        coluna.append(int(input(f'Digite um número inteiro para [{l}, {c}]: ')))
    lista.append(coluna[:])
    coluna.clear()
print(lista)
print('-='*20)
#while(l != 0 or c != 0):
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {lista[l][c]} ]', end='')
        if c == 2:
            print()
