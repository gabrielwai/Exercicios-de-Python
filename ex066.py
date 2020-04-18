quantidade = 0
soma = 0
while True:
    n = int(input('Digite um número inteiro (digite "999" para parar): '))
    if n == 999:
        break
    quantidade += 1
    soma += n
print(f'A soma dos {quantidade} números digitados é {soma}')
