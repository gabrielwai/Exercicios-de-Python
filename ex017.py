from math import sqrt
u = str(input('Qual a unidade de medida que será utilizada para o calculo da hipotenusa de um triângulo retângulo?: '))
op = float(input('Medida do cateto oposto: '))
adj = float(input('Medida do cateto adjacente: '))
print('A medida do cateto oposto é de {}{}, do cateto adjacente {}{} e a medida da hipotenusa é de {}{}.'.format(op,u,adj,u,sqrt(op**2+adj**2),u))