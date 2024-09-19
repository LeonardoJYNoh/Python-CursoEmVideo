#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

x = 0
soma = 0
while x != 999:
    x = int(input('Digite um número [999 para parar]: '))
    soma += x
soma -= x

print(soma)