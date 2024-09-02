l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l*h
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m^2'.format(l,h,a))

tinta = a/2
print('Para pintar essa parede, você precisará de {:.4f}l de tinta'.format(tinta))