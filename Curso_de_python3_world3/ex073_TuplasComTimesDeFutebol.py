""" Desafio 072
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Bragantino.
"""

msg = '           Tabela Brasileirão - 2023           '
m = len(msg)
print('\033[32m' + ('=' * m))
print(f'{msg}')
print(('=' * m) + '\033[m')

brasileirao = ('Botafogo', 'Palmeiras', 'Fluminense', 'Cruzeiro', 'Athletico-PR',
               'Atlético-MG', 'Santos', 'Fortaleza', 'Flamengo', 'São Paulo',
               'Grêmio', 'Internacional', 'Bragantino', 'Bahia', 'Goiás',
               'Vasco da Gama', 'Corinthians', 'Cuiabá', 'Coritiba', 'América-MG')
s = '-=' * 40
print(f'Os 5 Primeiros Colocados: {brasileirao[:5]}')
print(s)
print('Os 4 Últimos Colocados: ', brasileirao[-4:])
print(s)
print(f'Os Times em Ordem Alfabética: {sorted(brasileirao)}')
print(s)
print(f'Bragantino se encontra na {brasileirao.index("Bragantino")+1}º posição.')
