#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    valor = int(input('Quer ver a tabuada de qual valor'))
    if valor < 0:
        print('PROGRAMA TABUADA ENCERRADO. volte sempre!')
        break
    print('-'*20)
    x = 1
    while x <= 10:
        print(f'{valor} x {x} = {valor*x}')
        x += 1
    print('-'*20)