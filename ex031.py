from time import sleep
print('-=-' * 20)
print('Eu posso fazer o calculo do custo da sua viagem!')
print('-=-' * 20)
viagem = float(input('Qual é a distância da sua viagem? '))
print('Calculando...')
sleep(1)
if viagem <= 200:
    preco = viagem * 0.50

else: 
    preco = viagem * 0.45
print('O custo da sua viagem é de R$ {:.2f}'.format(preco))