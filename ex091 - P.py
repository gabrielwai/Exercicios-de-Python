import random
from time import sleep
jogos = dict()
lista = list()
print('Valores sorteados:')
for c in range(0, 4):
    jogos['nome'] = 'jogador' + str((c + 1))
    for j in range(0, 6):
        jogos['valor'] = random.randint(1, 6)
    sleep(.75)
    print(f'\tO {jogos["nome"]} tirou {jogos["valor"]}.')
    lista.append(jogos.copy())
    #jogos.clear()
print(lista)
print('O ranking dos jogadores foi:')
