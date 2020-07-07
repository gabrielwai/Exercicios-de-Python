import random
n1 = str(input('Digite o primeiro nome do aluno(a): '))
n2 = str(input('Digite o segundo nome do aluno(a): '))
n3 = str(input('Digite o terceiro nome do aluno(a): '))
n4 = str(input("Digite o quarto nome do aluno(a): "))
lista = [n1, n2, n3, n4]
print("O aluno sorteado é: {}".format(random.choice(lista)))