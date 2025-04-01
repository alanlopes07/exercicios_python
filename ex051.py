#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('=' * 20)
print('10 TERMOS de uma PA')
print('=' * 20)

num = int(input('Digite o 1º termo: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1 ) * razao
for c in range (num, decimo + razao, razao):
  print('{}'.format(c), end = ' -> ')
print('ACABOU!')



  