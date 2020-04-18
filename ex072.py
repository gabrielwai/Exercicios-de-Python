num_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
'nove', 'dez','onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
'dezenove', 'vinte')
num = 21
while num <0 or num >20:
    num = int(input('Digite um número entre zero a vinte incluindo-os: '))

    if num <0 or num>20:
        print('O número deve estar entre o intervalo de 0 a 20 incluindo-os.\nTente novamente.')

print('O número digitado foi ',end='')
print(f'{num_por_extenso[num]}.')
