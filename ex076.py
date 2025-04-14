'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

print('-=-' * 30)
print('LISTAGEM DE PREÇOS')
print('-=-' * 30)

listagem = ('Processador', 1500,
            'Placa de vídeo', 1700,
            'Memória Ram', 250,
            'Placa mãe', 750,
           'Fonte de alimentação', 400)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-=-' * 30)
print('FIM DA LISTAGEM')
