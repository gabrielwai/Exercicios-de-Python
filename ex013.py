p = float(input("Qual é o preço do produto? R$"))
d = int(5)
print('O preço do produto era de R${:.2f}, porém agora com desconto de {}% o preço passou a ser R${:.2f}'.format(p,d,p-((p*d)/100)))