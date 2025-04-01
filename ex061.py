#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('=' * 20)
print('10 TERMOS de uma PA')
print('=' * 20)

n = int(input('Digite o primeiro termo: '))
r = int(input('Razao: '))
termo = n
cont = 1 

while cont <= 10:
  print('{} --> '.format(termo), end = '')
  termo += r
  cont += 1 
print('FIM!')


  