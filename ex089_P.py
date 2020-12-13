geral = list()
alunos = list()
notas = list()
while True:
    continuar = 'A'
    alunos.append(str(input('Digite o nome de um aluno: ')))
    for n in range(1, 3):
          notas.append(float(input(f'Digite a {n}° nota do aluno: ')))
    alunos.append(notas[:])
    geral.append(alunos[:])
    notas.clear()
    alunos.clear()

    while not (continuar in 'SN'):
        continuar = (str(input('Deseja continuar [S/N]?: '))).strip().upper()[0]

        if (continuar in 'SN') == False:
            print('Valor inválido, tente novamente.')

    if continuar == 'N':
        break

#print(geral)
print('-='*20)
print('N°\tNome\tMédia')
print('-'*25)
for i, conteudo in enumerate(geral):
    print(f'{i}\t{conteudo[0]}\t{((conteudo[1][0])+(conteudo[1][1]))/2}')

while True:
    print('-' * 25)
    while True:
        del continuar
        continuar = -1
        while 0 > continuar or continuar > i:
            continuar = (int(input('Mostrar as notas de qual aluno? (999 para sair): ')))
            if (0 > continuar or continuar > i) and (continuar != 999):
                print('Valor fora do intervalo permitido. Tente novamente.')
        if continuar == 999:
             break
        print(f'As notas de {geral[continuar][0]} são: {geral[continuar][1]}')
        print('-' * 25)
print('Finalizando...',end='\n<<< Volte Sempre >>>\n')
