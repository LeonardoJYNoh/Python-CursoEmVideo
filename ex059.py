'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao != 5:
        print('Opção invalida')
    print('=-='*10)

