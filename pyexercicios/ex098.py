#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

from time import sleep

def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
         passo = 1 
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)

    print('-='*20)
    
    count = inicio
    if inicio < fim:
        while count <= fim:
            print(f'{count}', end=' ', flush= True)
            sleep(0.5)
            count += passo
    else:
        while count >= fim:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count -= passo
    print('FIM!')

contagem(0, 10, 1)
contagem(0, 10, 2)

print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contagem(inicio, fim, passo)