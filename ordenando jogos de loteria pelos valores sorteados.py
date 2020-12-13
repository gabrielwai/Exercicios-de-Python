import random
import operator

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
print(len(lista))
for c in range(len(lista)):
    print(f'{lista[c]["nome"]} => {lista[c]["valor"]}')
    lista[c]['valor'].sort()
print()
for c in range(len(lista)):
    print(f'{lista[c]["nome"]} => {lista[c]["valor"]}')
    lista[c]['valor'] = lista[c]['valor'][0]
print(lista,end='\n...\n')

#sorted(lista, key=operator.itemgetter(lista["valores"]))
#print(sorted(lista, key=operator.itemgetter()))
lista1.clear()
for c in range(len(lista)):
    lista1.append(lista[c]['valor'])
print(lista1)
lista1.sort()
print(lista1)
print(lista['nome'].index(lista1[0]))
for c in range(len(lista)):
    print(F'{lista.index(lista1[0])} = {lista1[0]}')
