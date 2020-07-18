from time import sleep
import random
jogos = list()

print('-'*20, end= 'JOGA NA MEGA SENA ')
print('-'*20)
N_jogos = int(input('Quantos jogos você quer que eu sortei?: '))
print('-='*3, end= f' SORTEANDO {N_jogos} JOGOS ')
print('-='*3)

for c in range(1, N_jogos+1):
    print(f'Jogo {c}: ', end='')
    for N in range(0, 7):
        numero = (random.randint(0, 60))
        while numero in jogos:
            numero = random.randint(0, 60)
        jogos.append(numero)
    print(jogos)
    jogos.clear()
    sleep(0.5)

print('-='*5, end=' < BOA SORTE! > ')
print('-='*5)
