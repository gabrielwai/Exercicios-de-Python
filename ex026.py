palavra = str(input('Digite uma palavra: ')).strip()
count = int
count = 0

print('Quantiade de letras "A": {}'.format(palavra.count('A')))
print('Aparece pela primeira vez na posição: {}'.format(palavra.find('A')))
#print(len(palavra))
while palavra[(len(palavra)-count-1)] != 'A':
    count = count + 1
print("'A' Aparece pela última vez na posição: {}".format(len(palavra)-count-1))
# WfaAf Afk Okgm KdmAdds