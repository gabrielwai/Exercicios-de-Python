lanbda = 5
while lanbda > 4 or lanbda < 1:
    lanbda = float(input('Digite um número real (entre 1 a 4 inclusive) que corresponderá ao lambda: '))
    if lanbda > 4 or lanbda < 1:
        print("Valor fora do intevalo (1 a 4). Tente novamente.")
Xn = 2
while Xn < 0 or Xn > 1:
    Xn = float(input('Digite um número (entre 0 a 1 inclusive) que corresponderá ao Xn: '))
    if Xn < 0 or Xn > 1:
        print("Valor fora do intevalo (0 a 1). Tente novamente.")

Xanterior = Xn
print(f"Xn = {Xn}")
for count in range(1, 32):
    print(f"Xn+{count} = {lanbda * Xanterior * (1 - Xanterior)}")
    Xanterior = lanbda * Xanterior * (1 - Xanterior)
