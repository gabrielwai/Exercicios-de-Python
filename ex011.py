altura = float(input('Digite a altura da parede em metros (m): '))
largura = float(input('Digite a largura da parede em metros (m): '))

print('A área da parede é de {} metros quadrados'.format(altura * largura),end=' ')
print('e a quantidade necessária de tinta para pinta-la por completo é de {:.2f} litros.'.format((altura * largura)/2))