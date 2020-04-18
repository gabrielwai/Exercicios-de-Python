salario = float(input('Qual é o salário do funcionário? R$'))
reajuste = int(15)
print("O salário antigo do funcionário era de R${:.2f}, com o reajuste de {}% o salário passou a ser de R${:.2f}.".format(salario,reajuste,salario+((salario*reajuste)/100)))