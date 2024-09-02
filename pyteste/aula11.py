print('\033[7;33;44mOlá mundo\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))


nome = 'Leonardo'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[4;34m'))

cores = {'limpa' : '\033[m',
         'azul': '\033[34m',
         'amarelo' : '\033[33m',
         'pretobranco' : '\033[m'}
