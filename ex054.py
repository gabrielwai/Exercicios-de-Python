cont = 1
maiores = [0, 0, 0, 0, 0, 0, 0]

dt_atual = int(input('Digite o ano atual: '))
#considerando a maioridade como 21 anos

for cont in range(1, 8):
    dt_nasc = int(input('Digite a data de nascimento da pessoa {}: '.format(cont)))
    if dt_atual - dt_nasc > 20:
        maiores[cont] = cont

print('As pessoas maiores de idade são: ')
for cont in range(0, 7):
    if maiores[cont] != 0:
        print(maiores[cont])

print("*Considerando a maioridade a partir dos 21 anos*")
