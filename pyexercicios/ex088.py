#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)

jogos = list()
jogada = list()

bilhetes = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, bilhetes):
    for j in range(0, 6):
        num = randint(1,60)
        while num in jogada:
            num = randint(1,60)
        jogada.append(num)
    jogada.sort()
    jogos.append(jogada[:])
    jogada.clear()

print('-=' * 3, f'SORTEANDO {bilhetes} JOGOS','-='*3)
for i in range(0,bilhetes):
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(1)