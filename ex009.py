n = int(input('Digite um número a ser calculada a tabuada: '))
print('-'*12)
for cont in range(1,11):
    print("{} x {} = {}".format(n,cont,n*cont))
print("-"*12)
