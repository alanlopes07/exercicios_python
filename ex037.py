#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

leitor = int(input('Digite um número inteiro: '))
print('Digite 1 para a base de conversão binária\nDigite 2 para a base de conversão octal\nDigite 3 para a base de conversão hexadecimal')
base = int(input('Qual será a base de conversão ? '))
if base == 1:
  print('Você escolheu fazer a conversão para binário! O número {} em binário é: {}'.format(leitor, bin(leitor) [2:]))
elif base == 2:
  print('Você escolheu fazer a conversão para octal! O número {} em octal é: {}'.format(leitor, oct(leitor) [2:]))
elif base == 3: 
  print('Você escolheu fazer a conversão para Hexadecimal! O número {} em Hexadecimal é: {}'.format(leitor, hex(leitor) [2:]))
else:
  print('Opção inválida!')