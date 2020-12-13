import random
from time import sleep
from operator import itemgetter
jogos = dict()
lista = list()
print('Valores sorteados:')
for c in range(0, 4):
    jogos['nome'] = 'jogador' + str((c + 1))
    for j in range(0, 6):
        jogos['valor'] = random.randint(1, 6)
    sleep(.60) # equivale a 0,60 segundos de pausa
    print(f'\tO {jogos["nome"]} tirou {jogos["valor"]}.')
    lista.append(jogos.copy()) #já sobrescreve os valores, por isso não precisa limpar ".clear()"
    #jogos.clear()
#print(lista)
print('  ==RANKING DOS JOGADORES==', end='\n')
lista.sort(key=itemgetter('valor'), reverse=True)
'''testando = sorted(lista, key=itemgetter("valor"))[-1] #"[-1]" = pega o último item da ordem crescente
print(f'TESTANDO : {testando}')'''
for n in range(len(lista)):
    sleep(.6)# equivale a 0,60 segundos de pausa
    print(f'  {n+1}° lugar: {lista[n]["nome"]} com {lista[n]["valor"]}')
