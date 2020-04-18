m = float(input('Digite uma medida em metros: '))
print('A medida digitada de {:.2f}m corresponde a:\n {:.2f}km\n {:.2f}hm\n {:.2f}dam\n {:.2f}dm\n {:.2f}cm\n {:.2f}mm.'.format(m, m*(10**-3),
m*(10**-2), m*(10**-1), m*10, m*(10**2), m*(10**3)))
