l1 = float(input('Digite o comprimento de um dos lados do triangulo: '))
l2 = float(input('Digite o outro comprimento do lado do triangulo: '))
l3 = float(input('Digite o último valor do último último lado do triângulo: '))

if l1 < (l2+l3):
    if l2 < l3:
        if l1 > l3-l2:
            print("\nOs três comprimentos podem formar um triângulo.")
        else:
            print('\nOs três comprimentos não podem formar um triângulo')
    else:
        if l1 > l2-l3:
            print("\nOs tres comprimentos podem formar um triângulo.")
        else:
            print('\nOs três comprimentos não podem formar um triângulo')
else:
    print('\nOs três comprimentos não podem formar um triângulo')
