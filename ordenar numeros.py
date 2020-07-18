from random import randint
ordenados = list()
lista = list()
for c in range(0, 5):
    lista.append(randint(1, 6))
print(f'Lista original: {lista}')

ordenados.append(lista[0])
#i = 1
'''f = 1
for i in range(0, f+1):
    verificador = 0
    if lista[i+1] < ordenados[i]:
        while (f-1) != i-1:
            ordenados[f] = ordenados[f-1]
        verificador = 1
    if verificador != 1:
        ordenados[f] = lista[i+1]
    #i+=1
    f += 1'''
quant_order = 1
quant_lista = len(lista)
while quant_order <= quant_lista:
    for c in range(0, quant_order+1):
        if lista[c+1] < ordenados[c]:
            while quant_order-1 >= c+1:
                ordenados[quant_order] = ordenados[quant_order-1]
            ordenados[quant_order-1] = lista[c+1]
        quant_order += 1

print(f'Ordenados: {ordenados}')
