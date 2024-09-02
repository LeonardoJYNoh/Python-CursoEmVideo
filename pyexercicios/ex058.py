#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi')

palpite = int(input('Qual é seu palpite? '))

tentativa = 1
while palpite != computador:
    if computador > palpite:
        print('Mais... Tente mais uma vez')
    elif computador < palpite:
        print('Menos... Tente mais uma vez')
    else:
        print('Opção invalida')
        tentativa -= 1
    tentativa += 1
    palpite = int(input('Qual é o seu palpite? '))

if tentativa == 1:
    print('Acertou na primeira tentativa. Parabéns!')
else:
    print('Acertou com {} tentativas. Parabéns!'.format(tentativa))