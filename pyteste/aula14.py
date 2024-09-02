#laços de repetição, (for)

'''for i in range(1, 6):
    print('oi')
print('FIM')'''
#repete oi 5 vezes e finaliza com um string "FIM"


'''for i in range(1, 6):
    print(i)
print('FIM')
#printa 1 até 5

for i in range(6, 0, -1):
    print(i)
print('FIM')
#printa 6 até 1

for i in range(0, 7, 2):
    print(i)
print('FIM')'''
#print 0 até 6 pulando 2 em 2



'''n = int(input('Digite um numero: '))
for i in range (0, n+1):
    print(i)
print('Fim')'''


'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')'''

'''for i in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')'''

s = 0
for i in range(0, 4):
    n = int(input('digite um valor: '))
    s += n
print('O somatorio de todos os valores foi {}'.format(s))