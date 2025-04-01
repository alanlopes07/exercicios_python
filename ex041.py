''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date

nasc = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - nasc 
if idade <= 9:
  print('Com {} anos de idade, você é da categoria MIRIM! '.format(idade))
elif idade > 9 and idade <= 14:
  print('Com {} anos de idade, você é da categoria INFANTIL! '.format(idade))
elif idade > 14 and idade <= 19:
  print('Com {} anos de idade, você é da categoria JUNIOR! '.format(idade))
elif idade > 19 and idade <= 25:
  print('Com {} anos de idade, você é da categoria SÊNIOR! '.format(idade))
else:
  print('Com {} anos de idade, você é da categoria MASTER! '.format(idade))