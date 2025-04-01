'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
'''
import random 
from time import sleep

print(' {:=^40} '.format(' PEDRA PAPEL E TESOURA '))
print('Suas escolhas: ')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
jogada = int(input('Qual a sua escolha ? '))
jogada_maquina = random.randint(1,3)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
if jogada == 1:
  print('Você escolheu PEDRA')
  if jogada_maquina == 2:
    print('Escolhi PAPEL, você perdeu!')
  elif jogada_maquina == 1:
    print('Também escolhi PEDRA, empatamos!')
  elif jogada_maquina == 3:
    print('Escolhi TESOURA, você ganhou!')
if jogada == 2: 
  print('Você escolheu PAPEL')
  if jogada_maquina == 1:
    print('Escolhi PEDRA, você ganhou!')
  elif jogada_maquina == 2:
    print('Também escolhi PAPEL, empatamos!')
  elif jogada_maquina == 3:
    print('Escolhi TESOURA, você perdeu! ')
if jogada == 3:
  print('Você escolheu TESOURA')
  if jogada_maquina == 1:
    print('Escolhi PEDRA, voce perdeu!')
  elif jogada_maquina == 2:
    print('Escolhi PAPEL, você venceu!')
  elif jogada_maquina == 3:
    print('Também escolhi TESOURA, empatamos!')
else: 
  print('Escolha uma opção válida!')
  
  