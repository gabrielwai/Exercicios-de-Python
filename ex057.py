sexo = str(input('Digite um sexo [M/F]: ')).strip().lower()[0]
#while sexo not in 'MmFm':
while sexo not in 'mf':
    sexo = str(input('Dados inválidos. Tente novamente.\nDigite um sexo [M/F]: ')).strip().lower()[0]
print('Sexo ({}) cadastrado com sucesso!'.format(sexo.upper()))
