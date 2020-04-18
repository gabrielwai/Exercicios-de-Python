from random import choice, shuffle
n1 = str(input('Digite o nome do(a)  primeiro(a) estudante: '))
n2 = str(input('Digite o nome do(a)  segundo(a) estudante: '))
n3 = str(input('Digite o nome do(a)  terceiro(a) estudante: '))
n4 = str(input('Digite o nome do(a)  quarto(a) estudante: '))
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem das apresentações dos trabalhos será: {}'.format(alunos))