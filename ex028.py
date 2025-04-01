from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
palpite = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(3)
sorteio = randint(0, 5)
if palpite == sorteio:
    print('Parabéns você acertou!')

elif palpite < 0 or palpite > 5:
    print('Você pensou em um número fora do intervalo permitido!')

else:
    print('Você errou! O número pensado foi {} '.format(sorteio))