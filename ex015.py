km = float(input('Qual a quantidade percorrida em kilometros? '))
dias = int(input('Durante quantos dias o carro foi alugado?: '))
print('O carro percorreu {}Km durante {} dias. Portanto o preço a se pagar pelo aluguel é de R${:.2f}'.format(km,dias,60*dias+0.15*km))
