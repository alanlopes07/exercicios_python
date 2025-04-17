''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
'''

valores = []

while True: 
  v = int(input('Digite um valor:'))
  if v not in valores:
    valores.append(v)
    print('Valor armazenado com sucesso!')
  else:
    print('Valor duplicado, por isso não será armazenado.')
  mantem = str(input('Deseja continuar ? [S/N] '))
  if mantem == 'n' or mantem == 'N':
    break
print(f'Os valores armazenados foram {valores}')
valores.sort()
print(f'Assim ficam os valores armazenados em ordem crescente {valores}')  
