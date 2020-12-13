from time import sleep


def contagem(i, f, p):
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    contagem = i
    p = abs(p)
    #"notnull" serve para impedir que "abs((f-i)" seja igual a zero, ou seja, divizão por zero

    notnull = i == f
    limite = (f-i)/(abs((f-i)+notnull)) #se ordem crescente, então: 1 ; se ordem decrescente, então: -1 ; se iguais (f = i), então: 0

    p += not(1 & bool(p)) #se p != 0, então: p += 0  ;  se p == 0, então: p += 1
    p *= limite #"limite" serve para ajustar o sinal (+,-) do passo, que depende da ordem da PA
    p += not(limite)

    for c in range(i, f + int(limite), int(p)):
        sleep(0.25)
        print(f'{contagem:.0f}', end=' ')
        contagem += p
    print('FIM!')
    print('-='*30)



print('-='*30)
contagem(1,10,1)
contagem(10,0,2)
print(f'Agora é sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(início, fim, passo)
