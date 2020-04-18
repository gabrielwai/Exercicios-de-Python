lista = list()
quantidade = 0
continuar = ''
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    quantidade += 1

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        continuar = continuar[0]

        if continuar != 'S' and continuar != 'N':
            print('Valor inválido, tente novamente')

    if continuar == 'N':
        break

    continuar = ''

lista.sort(reverse=True)
print(f'A quantidade de números digitados foi {quantidade}')
print(f'A lista preenchida (de forma decrescente) é: {lista}')

if 5 in lista:
    print(f"O número 5 foi digitado e está na lista na {len(lista)-lista.index(5)-lista.count(5)+1}ª posição (na"
          f" ordem crescente) e na {lista.index(5)+1}ª posição na \nordem decrescente (como está sendo mostrado)."
          f" Considerando a primeira aparição.")
else:
    print("O número 5 não foi digitado.")
