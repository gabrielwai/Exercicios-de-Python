nome = str(input('Digite seu nome completo: ')).strip()
count = int
count = 0
count2 = int
count2 = 0
#nome.split()
print('Seu primeiro nome é: {}'.format(nome.split()[0]))

while count != len(nome)-1:
    if(nome[count] == ' '):
        count2 = count
    count = count+1

print('O seu último nome é: {}'.format(nome[count2+1:]))
#print(nome[count2+1:])
#print(nome.find(' '))

#João Ferreira da Silva