from time import sleep
repetirtudo = 1
repetir = 1

while repetirtudo == 1:

    repetir = 1
    num1 = int(input('Digite um valor numérico inteiro: '))
    num2 = int(input('Digite agora um segundo valor: '))

    while repetir == 1:

        print('\nMenu de Operações:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair\n')
        menu = int(input('Que operação queres realizar?: '))

        if menu == 1:
            print('A opção escolhida foi "soma", portanto: {} + {} = {}'.format(num1,num2,num1 + num2))

        elif menu == 2:
            print('A opção escolhida foi "multiplicar", portanto: {} x {} = {}'.format(num1, num2, num1 * num2))

        elif menu == 3:
            if num1 > num2:
                print('A opção escolhida foi "maior", portanto: {} > {}'.format(num1, num2))
            elif num2 > num1:
                print('A opção escolhida foi "maior", portanto: {} > {}'.format(num2, num1))
            else:
                print('A opção escolhida foi "maior", portanto: {} = {}'.format(num1, num1))

        elif menu == 4:
            print('A opção escolhida foi "novos números", portanto: Digites novos números.')
            repetir = 0

        elif menu == 5:
            print('A opção escolhida foi "sair", portanto: saindo', end="")
            sleep(0.75)
            print('.', end='')

            for c in range(0, 2):
                sleep(1.5)
                print('.', end='')

            repetirtudo = 0
            repetir = 0

        else:
            print('Por favor, digite um valor válido. Tente novamente.')

        sleep(2)
