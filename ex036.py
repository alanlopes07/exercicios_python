valor_casa = float(input('Digite o valor da casa: '))
salario_comprador = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = valor_casa / (anos * 12)
if prestacao > salario_comprador * 30 / 100:
  print('Para pagar uma casa de {:.2f}R$ em {} anos a prestação será de {:.2f}R$ Empréstimo NEGADO!'.format(valor_casa, anos, prestacao))
else:
  print('Para pagar uma casa de {:.2f}R$ em {} anos a prestação será de {:.2f}R$ Empréstimo pode ser CONCEDIDO!'.format(valor_casa, anos, prestacao))