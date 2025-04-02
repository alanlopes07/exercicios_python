'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('=' * 30)
print('Banco Lopes')
print('=' * 30)

valor = int(input('Qual valor deseja sacar? R$: '))
total = valor
cedula_atual = 50 
total_cedulas = 0

while True:
  if total >= cedula_atual:
    total -= cedula_atual
    total_cedulas += 1
  else:
    print(f'Total de {total_cedulas} cédulas de R$: {cedula_atual}')
    if cedula_atual == 50:
      cedula_atual = 20
    elif cedula_atual == 20:
      cedula_atual = 10
    elif cedula_atual == 10:
      cedula_atual = 1
    total_cedulas = 0
    if total == 0:
        break
print('Volte sempre!')