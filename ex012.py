preco = float(input('Qual é o preço do produto? R$:'))
desconto = preco - (preco * 5 / 100)
print('O produto que custava{}, na promoção com desconto de 5% vai custar {:.2f}'.format(preco, desconto))