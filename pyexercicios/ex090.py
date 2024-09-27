#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.



dados = dict()
dados['nome'] = input('Nome: ')
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
if dados['média'] >= 7:
    dados['situação'] = 'Aprovado'
elif dados['média'] >= 5:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Repovado'


print('-='*30)
for i, j in dados.items():
    print(f'  - {i} é igual a {j}')