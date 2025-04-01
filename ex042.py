'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''
from math import radians, sin, cos, tan

print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
r1 = float(input('Informe a primeira reta: '))
r2 = float(input('Informe a segunda reta: '))
r3 = float(input('Informe a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Os segmentos acima PODEM FORMAR um triângulo', end ='')
  if r1 == r2 == r3:
    print('EQUILATERO!')
  elif r1 != r2 != r3 != r1:
    print('ESCALENO!')
  else:
    print('ISÓSCELES!')
else:
  print('Os segmentos acima NÃO PODEM FORMAR um triângulo')