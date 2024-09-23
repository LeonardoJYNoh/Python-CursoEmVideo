'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Grêmio.
'''

times = ('Botafogo','Palmeiras','Fortaleza','Flamengo','São Paulo','Bahia','Cruzeiro','Internacional','Atlético Mineiro','Vasco','Juventude','Grêmio','Athletico-PR','Bragantino','Criciúma','Vitória','Corithians','Fluminense','Cuiaba','Atlético Goiano')
#29/09/2024

print('-='*20)
print(f'Lista de times do Brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiros são {times[0:6]}')
print('-='*20)
print(f'os 4 ultimos são {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*20)
print(f'O Grêmio está na {times.index("Grêmio")+1}° posição')