import math
ângulo = float(input('Digite um ângulo: '))
print('O seno do ângulo {} é {:.2f}'.format(ângulo,math.sin(math.radians(ângulo))))
print('O cosseno do ângulo {} é {:.2f}'.format(ângulo, math.cos(math.radians(ângulo))))
print('A tangente do ângulo {} é {:.2f}'.format(ângulo, math.tan(math.radians(ângulo))))