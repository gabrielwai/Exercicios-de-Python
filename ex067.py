
while True:
    n = int(input('Quer ver a tabuada de qual valor? (digite qualquer valor negativo para sair): '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n*c}')
print('-'*10, end=' Fim ')
print('-'*10)
