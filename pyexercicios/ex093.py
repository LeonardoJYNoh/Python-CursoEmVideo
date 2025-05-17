#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()

jogador['nome'] = input('Nome do Jogador: ')
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

partidas = list() 
total = 0
for i in range(0, jogos):
    partidas.append(int(input(f'   Quantos gols na partida {i+1}? ')))
jogador['gols'] = partidas
jogador['total'] = sum(partidas)

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador Zico jogou {jogos} partidas')
for i in range(0, jogos):
    print(f'  => Na partida {i+1}, fez {partidas[i]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
