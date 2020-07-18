from random import randint
from operator import itemgetter, attrgetter
print('Valores Sorteados: ')
jogadores = dict()
lista = list()
for c in range(0, 4):
    jogadores['identificador'] = c+1
    jogadores['valor'] = randint(1, 6)

    print(F'O jogador{jogadores["identificador"]} tirou {jogadores["valor"]}')
    lista.append(jogadores.copy())
print(f'Dicionário: {jogadores}')
print(f'Lista: {lista}')
print('Segue a seguir a ordenação de valores:', end="\n")
ordenados = list()
ordenados.append(lista[0]['valor'])
for c in range(0, 4):
    if lista[c+1]['valor'] < ordenados[c]:
        for pra_frente in range(3, c+1, -1):
            ordenados[c+1] = ordenados[c]

