#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

print('Digite um número para')
fato = int(input('calcular seu Fatorial: '))

multi = 1
if fato == 0:
    print('O fatorial de 0 é 1')
elif fato > 0:
    print('Calculando {}! ='.format(fato, fato), end=' ')
    while fato > 0:
        print('{}'.format(fato), end = '')
        print(' x ' if fato > 1 else ' = ', end='')
        multi = multi * fato
        fato -= 1
    print(multi)