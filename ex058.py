import random
numero = random.randint(0,10)
tentativas = 1
#usuario = numero + 1

usuario = int(input('Tente acertar qual é o número que o computador pensou (de 0 a 10): '))

while usuario != numero:
    usuario = int(input('Você errou. Tente novamente acertar qual é o número que o computador pensou (de 0 a 10): '))
    tentativas += 1

print("Parabéns você acertou! com apenas {} tentativas.".format(tentativas))
