geral = list()
alunos = list()
continuar = 'A'
while True:
    alunos.append(str(input('Digite o nome de um aluno: ')))
    for n in range(1, 3):
          alunos.append(float(input(f'Digite a {n}° nota do aluno: ')))
    geral.append(alunos[:])
    alunos.clear()

    while continuar in 'SN' == False:
        continuar = (str(input('Deseja continuar [S/N]?: '))).strip().upper()[0]

        if continuar in 'SN' == False:
            print('Valor inválido, tente novamente.')

    if continuar == 'N':
        break
print(geral)