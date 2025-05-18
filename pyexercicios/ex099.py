#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(* num):
    count = maior = 0
    print('-=' * 30)
    print('Analisando os valores passado... ')
    for i, valor in enumerate(num):
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if i == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        count += 1
    print(f'Foram informados {count} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(6)