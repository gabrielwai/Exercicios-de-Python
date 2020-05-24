import math
n = -1
while n < 0:
    n = int(input('Digite um número (N) inteiro a se calcular seu fatorial: '))
    '''print(f"O Fatorial de N é = {math.factorial(n)} = N!")'''
    if n < 0:
        print("Digite apenas valores positivos. Tente novamente.",end='\n')

if n == 0:
    fatorial = 1
else:
    fatorial = n
    for count in range(1, n-1):
        fatorial *= (n-count)

print(f"N! = {fatorial}")
acumulador = fatorial
count = 0
while fatorial / 10 > 1:
        fatorial /= 10
        count += 1
count += 1
print(f'Número de algarismos de N! = {count}')

fatorial = acumulador
acumulador = 0
print(f'Fatorial = {fatorial} ; Acumulador = {acumulador}')

for j in range(1, count+1):
    acumulador += math.floor((fatorial - ((math.floor(fatorial/math.pow(10, j))) * math.pow(10, j))) / math.pow(10, j-1))

    print(f"Soma dos algarismos: {acumulador} ; {math.floor((fatorial - ((math.floor(fatorial/math.pow(10, j))) * math.pow(10, j))) / math.pow(10, j-1))} ; j = {j}")

    print(f"n/10^{j} = {(math.floor(fatorial/math.pow(10, j)))}")
    print(f"n * 10^{j} = {((math.floor(fatorial/math.pow(10, j))) * math.pow(10, j))}")
    print(f"n - ((n/10^{j})*10^{j}) = {(fatorial - ((math.floor(fatorial/math.pow(10, j))) * math.pow(10, j)))}")

print(f"Resultado da soma dos algarismos: {acumulador}")
