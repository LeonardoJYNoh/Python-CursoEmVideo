#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

cont = 0

while True:
    print('=-='*10)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-='*10)
    jogada = int(input('Diga um valor: '))
    escolha = input('Par ou Ímpar [P/I] ').upper().strip()[0]
    computador = randint(0, 10)
    soma = jogada + computador
    if escolha == 'P':
        opcao = 'par'
    else:
        opcao = 'impar'
    if (escolha in 'Pp' and soma%2 == 0) or (escolha in 'Ii' and soma%2 != 0):
        print('-'*30)
        print(f'Você jogou {jogada} e o computador {computador}. Total de {jogada+computador} DEU {opcao}')
        print('-'*30)
        print('Você PERDEU!')
        print('=-='*10)
        print(f'Game OVER! Você venceu {cont} vezes')
        break
    else:
        print('-'*30)
        print(f'Você jogou {jogada} e o computador {computador}. Total de {jogada+computador} DEU {opcao}')
        print('-'*30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    