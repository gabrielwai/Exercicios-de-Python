aluno = dict()
aluno['nome'] = str(input('Digite o nome do(a) aluno(a): '))
while True:
    aluno['média'] = float(input('Digite a média: '))

    if 0 > aluno['média'] or aluno["média"] > 10:
        print('Valor fora do intervalo. Tente novamente.')
    else:
        break

print('='*30)
print(f'O nome do aluno(a) é {aluno["nome"]} e a média é {aluno["média"]}')
print('A situação é igual a ',end="")

if aluno["média"] >= 7:
    aluno["situação"] = 'Aprovado(a)'
elif 7 > aluno["média"] >= 5:
    aluno["situação"] = 'Recuperação'
else:
    aluno["situação"] = 'Reprovado(a)'

print(f'{aluno["situação"]}.')
