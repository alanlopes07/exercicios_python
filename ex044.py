'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
import math
preco = float(input('Informe o preço dos produtos: '))
print('[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ]3x ou mais no cartão')
opcao = int(input('Qual a opção? '))
if opcao == 1:
  desconto = preco * 0.10
  preco_final = preco - desconto
  print('Você tem um desconto de 10%\nSua compra sairá pelo preço de R$: {:.2f}'.format(preco_final))
elif opcao == 2:
  desconto = preco * 0.05
  preco_final = preco - desconto
  print('Você tem um desconto de 5%\nSua compra sairá pelo preço de R$: {:.2f}'.format(preco_final))
elif opcao == 3: 
  desconto = preco
  preco_final = desconto
  print('Você não possui nenhum desconto com essa opção\nSua compra sairá pelo preço de R$: {:.2f}'.format(preco_final))
elif opcao == 4:
  juros = preco * 0.20
  preco_final = preco + juros
  print('Você poderá fazer essa compra com um juros de 20%\nSua compra sairá pelo preço de R$: {:.2f}'.format(preco_final))