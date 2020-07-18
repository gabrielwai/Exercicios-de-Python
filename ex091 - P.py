import random
jogos = dict()

for c in range(0, 4):
    jogos['nome'] = 'jogador' + str((c + 1))
    for j in range(0, 6):
        jogos['valor'] = random.randint(1, 6)
    print(jogos)
    #jogos.clear()
print(jogos)
