def escreva(msg):
    print('~'*(len(msg) + 2))
    print(f' {msg}')
    print('~' * (len(msg) + 2))


mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)
