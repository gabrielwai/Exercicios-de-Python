print('='*10,end='')
print('Cadastros de Usuários',end='='*10)
acimade18 = 0
contMasculino = 0
contFeminino = 0
MenosdeVinte = 0
continuar = 'S'

while True:
    nome = str(input("\nDigite o nome da pessoa: ")).strip().title()

    idade = -1
    while idade < 0:
        idade = int(input("Digite a idade: "))
        if idade < 0:
            print('Idade não pode ser nagetiva. Tente novamente.')

    sexo = 'A'
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
        if sexo != 'M' and sexo != 'F':
            print('Valor inválido. Tente novamente.')

    if idade >= 18:
        acimade18 += 1
    if sexo[0] == 'M':
        contMasculino += 1
    else:
        contFeminino += 1
        if idade < 20:
            MenosdeVinte += 1

    continuar = 'A'
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("\nDeseja continuar cadastrando? [S/N]: ")).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('Valor inválido, tente novamente.')

    if continuar[0] == 'N':
        break
    elif continuar[0] != 'S':
        print('Valor inválido. Tente novamente.')

print(f'\nAs pessoas maiores de 18 anos são: {acimade18}')
print(f'A quantidade de pessoas do sexo masculino cadastradas é de {contMasculino}')
print(f'A quantidade de mulheres cadastradas com menos de vinte anos é {MenosdeVinte}')
