''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
print('-' * 30)
print('ALAN INFORMÁTICA')
print('-' * 30)
cont_preco = total = prod1000 = 0
prod_barato = float('inf')
nome_prod_barato = ' '
while True:
  produto = str(input('Nome do produto: '))
  preco = float(input('Preço R$: '))
  cont_preco += preco
  if preco < prod_barato:
    prod_barato = preco
    nome_prod_barato = produto
  if preco > 1000:
    prod1000 += 1
  mantem = ' '
  while mantem not in 'SN':
    mantem = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
  if mantem == 'N':
    total = cont_preco 
    print(f'O total gasto na compra foi de R$: {total:.2f}. O número de produtos acima de R$:1000,00 foi de {prod1000} e o produto mais barato foi {nome_prod_barato} custando R$:{prod_barato}')
    break
print('FIM')
