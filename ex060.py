#Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial
from time import sleep

n  = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end = '')
sleep(1)
while c > 0:
  print('{} '.format(c), end = '')
  print('x ' if c > 1 else '= ', end = '')
  f *= c
  c -= 1
print('{}'.format(f))