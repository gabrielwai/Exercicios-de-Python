jogador = dict()
lista = list()
gols = []
while True:
    print("-" * 30)
    jogador["nome"] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))

    for c in range(jogador['partidas']):
        gols.append(int(input(f"Quantos gols na partida {c+1}?: ")))

    jogador['gols'] = gols.copy()
    lista.append(jogador.copy())
    gols.clear()
    print(lista)
    continuar = str(input(f'Desseja-te continuar [S/N]?: ')).strip()[0].upper()

    if continuar in 'N':
        break

print('-='*30)
print(f'{"cod":<4}{"nome":<22}{"gols":<15}{"total"}\n',end='-'*60)
print()

for count in range(len(lista)):
    print(f' {count:<3}{lista[count]["nome"]:<19}  {lista[count]["gols"]}',end='')
    tabulação = 18 - ((len(lista[count]["gols"])-1)*2 + 2 + len(lista[count]["gols"]))

    if tabulação < 0:
        tabulação = 0

    for i in range(tabulação):
        print(' ',end='')
    print(f'{sum(lista[count]["gols"]):>2}')

while True:
    cod = int(input('Mostrar dados de qual jogador?[cod]: '))

    while (cod >= len(lista) or cod < 0) and cod != 999:
        print('Valor fora do intervalo, tente novamnte.')
        print('-'*30)
        cod = int(input('Mostrar dados de qual jogador?[cod]: '))

    if cod == 999:
        break

    print(f'-- Levantando dados do jogador {lista[cod]["nome"]}:')
    for count in range(len(lista[cod]["gols"])):
        print(f'   No jogo {count} fez {lista[cod]["gols"][count]} gols.')
    print('-'*60)

print('--ENCERRANDO--')
