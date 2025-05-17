jogadores = list()
jogador = dict()
jogos = list()

while True:
    jogador.clear()
    jogos.clear()
    jogador['nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range (0, partidas):
        jogos.append(int(input(f'Quantos gols na partida {i+1}?')))
    jogador['gols'] = jogos[:]
    jogador['total'] = sum(jogos)
    jogadores.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    
    if cod == 999:
        break
    if cod >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {cod}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}:')
        for i, g in enumerate(jogadores[cod]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')