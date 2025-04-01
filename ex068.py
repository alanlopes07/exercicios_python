#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
v = 0
while True:
  jogador = int(input('Diga um valor: '))
  computador = randint(0,10)
  total = jogador + computador 
  tipo = ' '
  while tipo not in 'PI':
    tipo = str(input('Par ou ímpar ?')).strip().upper()[0]  
  print(f'Você jogou {jogador} e o computador {computador}. total de {total}')
  print('Deu par' if total % 2 == 0 else 'Deu ímpar')
  if tipo == 'P':
    if total % 2 == 0:
      print('Você venceu!')
      v += 1 
    else: 
      print('Você perdeu!')
      break
  elif tipo == 'I':
    if total % 2 != 0:
      print('Você venceu!')
      v +=1
    else:
      print('Você perdeu!')
      break
  print('Vamos jogar novamente...')
print(f'Você ganhou um total de {v} vezes')  


