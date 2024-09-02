#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#primiera versão
'''print('='*30)
print(' '*5 + '10 TERMOS DE UMA PA' + ' '*5)
print('='*30)

pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

print('{} >'.format(pt), end=' ')
for i in range(0, 9):
    print('{} >'.format(pt+razao), end=' ')
    pt += razao
print('ACABOU')'''

#Versão mais otimizado
print('='*30)
print(' '*5 + '10 TERMOS DE UMA PA' + ' '*5)
print('='*30)

pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = pt + (10 - 1) * razao

for i in range(pt, decimo + razao, razao):
    print(i, end=' > ')
print('ACABOU')