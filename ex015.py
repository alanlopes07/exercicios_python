dias = int(input('Digite quantos dias alugou o carro: '))
km = float(input('Digite quantos km rodou com o carro: '))
total = (60 * dias) + (0.15 * km)
print('O total a pagar é de R$:{:.2f}'.format(total))