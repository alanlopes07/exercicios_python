from datetime import date
atual = date.today().year
ano = int(input('Digite o ano que você nasceu: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos.'.format(ano, idade))
alistamento = ano + 18
if idade < 18:
  print('Você tem até o ano de {} para se alistar!'.format(alistamento))
elif idade == 18:
  print('Você está no ano limite para se alistar!')
else:
  print('Você deveria ter se alistado no ano de {} !'.format(alistamento))