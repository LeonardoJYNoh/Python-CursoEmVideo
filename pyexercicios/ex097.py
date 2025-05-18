#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(palavra):
    print('~~'+'~'*len(palavra)+'~~')
    print(f'  {palavra}')
    print('~~'+'~'*len(palavra)+'~~')
escreva('Olá Mundo!')