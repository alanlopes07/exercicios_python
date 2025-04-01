#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um número para ver sua tabuada: '))
print('A tabuada de {} é: '.format(num))
for c in range (1 , 11):
  print('{} x {} = {}'.format(num, c, num * c))