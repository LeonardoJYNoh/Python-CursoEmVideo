nome = input('Digite seu nome completo: ').strip()
n = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[-1]))
#n[len(nome) - 1]