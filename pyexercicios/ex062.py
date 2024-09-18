#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-='*10)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

y = 1
x = 10
soma = p1
termos = 0

while y > 0:
    termos += x
    while x > 0:
        print(soma, end=' > ')
        soma += razao
        x -= 1
    print('PAUSA')
    y = int(input('Quantos termos você quer mostrar mais? '))
    x = y
print('Progressão finalizada com {} termos mostrados'.format(termos))