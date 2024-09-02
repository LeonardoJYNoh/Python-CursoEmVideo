import math

angulo = math.radians(float(input('Digite o ângulo que você deseja: ')))

print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(angulo, math.sin(angulo)))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(angulo, math.cos(angulo)))
print('O ângulo de {:.1f} tem o TANGENTE de {:.2f}'.format(angulo, math.tan(angulo)))