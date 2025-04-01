'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
from time import sleep
print('-=-' * 20)
print('CALCULO DE IMC')
print('-=-' * 20)

nome = str(input('Informe seu nome: '))
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2) 
print('OK {}, vou calcular seu IMC...'.format(nome))
sleep(2)
if imc < 18.5:
  print('Seu imc é {:.2f}, portanto você está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc <= 25:
  print('Seu IMC é {:.2f}, portanto você está no peso ideal!'.format(imc)) 
elif imc >= 25 and imc <= 30:
  print('Seu IMC é {:.2f}, portanto você está com sobrepeso!'.format(imc))
elif imc > 30 and imc <= 40:
  print('Seu IMC é de {:.2f}, portanto você está na condição de obesidade!'.format(imc))
else:
  print('Seu IMC é de {:.2f}, portanto você está na condição de obesidade mórbida!'.format(imc))