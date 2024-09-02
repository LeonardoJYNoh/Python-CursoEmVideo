import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hip = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hip))