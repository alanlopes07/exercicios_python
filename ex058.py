#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10, tente adivinhar...')
print('-=-' * 20)
tentativas = 1
palpite = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(1)
sorteio = randint(0, 10)
while palpite < 0 or palpite > 10:
  palpite = int(input(('Número invalido! Por favor digite um número entre 0 e 10: ')))
  print('processando...')
  sleep(1)
while palpite != sorteio:
  tentativas +=1
  if palpite > sorteio:
    palpite = int(input('Errou! Pensei em um número menor: '))
    print('Processando...')
    sleep(1)
  if palpite < sorteio:
    palpite = int(input('Errou! Pensei em um número maior: '))
    print('processando...')
    sleep(1)
print('Parabéns, você acertou! foram necessárias {} tentativas para você acertar'.format(tentativas))