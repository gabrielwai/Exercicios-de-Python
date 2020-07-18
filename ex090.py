aluno = dict()
aluno['nome'] = str(input('Digite o nome do(a) aluno(a): '))
while True:
    aluno['média'] = float(input('Digite a média: '))

    if 0 > aluno['média'] or aluno["média"] > 10:
        print('Valor fora do intervalo. Tente novamente.')
    else:
        break

print(f'O nome do aluno(a) é {aluno["nome"]} e a média é {aluno["média"]}')
print('A situação é igual a ',end="")
if aluno["média"] < 7:
    print('Reprovado(a).')
else:
    print('Aprovado(a)!')
