"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
"""

x1 = int(input('Primeiro valor: '))
x2 = int(input('Segudno valor: '))

opcao = 0

while opcao != '5':
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
''')
    opcao = input('>>>>> Qual é a sua opção? ')
    if opcao == '1':
        print('A soma entre {} + {} é {}'.format(x1, x2, x1+x2))
    elif opcao == '2':
        print('A multiplicação entre {} x {} é {}'.format(x1, x2, x1*x2))
    elif opcao == '3':
        if x1 > x2:
            print('Entre {} e {} o maior é {}'.format(x1, x2, x1))
        else:
            print('Entre {} e {} o maior é {}'.format(x1, x2, x2))
    elif opcao == '4':
        print('Infome os números novamente:')
        x1 = int(input('Primeiro valor: '))
        x2 = int(input('Segundo valor: '))
    elif opcao == '5':
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)