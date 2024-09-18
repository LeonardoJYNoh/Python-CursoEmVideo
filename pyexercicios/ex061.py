#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA')
print('-='*10)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

x = 10
soma = p1
while x > 0:
    print(soma, end=' > ')
    soma += razao
    x -= 1
print('FIM')
