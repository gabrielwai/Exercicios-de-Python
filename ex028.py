import random
N = random.randint(1,5)
n = int(input('Tente acertar o número (entre 1 e 5, incluindo-os) que o computador pensou: '))
if n == N:
    print('Parabéns!, você acertou.')
else:
    print("Você errou.")