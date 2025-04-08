'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

tabela = ('Flamengo', 'Internacional', 'São Paulo', 'Atlético-MG', 'Palmeiras', 'Grêmio', 'Santos', 'Corinthians', 'Athletico-PR', 'Fortaleza', 'Ceará SC', 'Bahia', 'Atlético-GO', 'Sport Recife', 'Vasco da Gama', 'Botafogo', 'Chapecoense','Vitória', 'Mirassol', 'América MG')

print('-=' * 30)

print(f'Lista dos 20 times do Campeonato Brasileiro : {tabela} ')
print('-=' * 30)

print(f'Os 5 primeiros times são: {tabela[:5]}')
print('-=' * 30)

print(f'Os 4 últimos colocados são {tabela[16:20]}')

print('-=' * 30)

print(f'Os times em ordem alfabética fica da seguinte maneira: {sorted(tabela)}')

print('-=' * 30)

print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')