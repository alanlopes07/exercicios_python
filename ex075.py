'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: '))
       )


print(f'Os valores digitados foram {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
  print(f'O valor 3 foi digitado na {num.index(3)+1}ª posição')
else: 
 print('O valor 3 não foi digitado')
print(f'Os valores pares foram ', end = '')
for n in num:
 if n % 2 == 0:
  print(n, end = ' ')
