pessoas = list()
auxiliar = list()
maisleve = list()
maispesada = list()
continuar = ''

auxiliar.append(str(input('Nome: ')))
auxiliar.append(float(input('Peso: ')))

menorPeso = auxiliar[1]
#maisleve.append(auxiliar[0])
maiorPeso = auxiliar[1]
#maispesada.append(auxiliar[0])
pessoas.append(auxiliar[:])
auxiliar.clear()

while True:

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        continuar = continuar[0]

        if continuar != 'S' and continuar != 'N':
            print('Valor inválido, tente novamente.')

    if continuar == 'N':
        break

    continuar = ''

    auxiliar.append(str(input('Nome: '))) # captalize()
    auxiliar.append(float(input('Peso: ')))

    if auxiliar[1] < menorPeso:  # (len(auxiliar) - 1) = 1
        menorPeso = auxiliar[1]
        #maisleve.insert(0, auxiliar[0])
    elif auxiliar[1] > maiorPeso:
        maiorPeso = auxiliar[1]
        #maispesada.append(auxiliar[0])

    print(f'maiorPeso: {maiorPeso:.2f}')
    print(f'menorPeso: {menorPeso:.2f}')

    pessoas.append(auxiliar[:])
    auxiliar.clear()

for p in pessoas:
    if p[1] == maiorPeso:
        maispesada.append(p[0])
    elif p[1] == menorPeso:
        maisleve.append(p[0])
print(pessoas)
print(f'A quantidade de pessoas cadastradas é: {len(pessoas)}')
print(f'O menor peso encontrado foi de {menorPeso:.2f}, as pessoas que possuem este peso são: {maisleve}')
print(f'O maior peso encontrado foi de {maiorPeso:.2f}, as pessoas que possuem este peso são: {maispesada}')
