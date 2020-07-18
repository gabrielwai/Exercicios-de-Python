import random

jogos = dict()
lista = list()
lista1 = list()
for c in range(0, 4):
    jogos['nome'] = 'jogador' + str((c + 1))
    for j in range(0, 6):
        while True:
            n = random.randint(1, 60)
            print(f'{lista1} ; {n}')
            if n not in lista1:
                lista1.append(n)
                break
    jogos['valor'] = lista1.copy()
    lista1.clear()
    lista.append(jogos.copy())
    print(jogos)
    jogos.clear()
print(jogos)
print(lista)
print(lista1)
