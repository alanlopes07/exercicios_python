'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''
valores = []
for v in range (0,5):
  valores.append(int(input(f'Digite um valor: ')))
print(f'O comprimento da lista foi de {len(valores)}. O maior valor foi: {max(valores)}. Já o menor valor foi: {min(valores)}')
