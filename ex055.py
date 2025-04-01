#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesoMaior = 0
pesoMenor = float('inf')
for pessoas in range(1, 6):
  peso = float(input('Peso da {}ª pessoa: '.format(pessoas)))
  if peso > pesoMaior:
    pesoMaior = peso
  if peso < pesoMenor:
    pesoMenor = peso
print('O maior peso foi {:.2f} kg'.format(pesoMaior))
print('O menor peso foi {:.2f} kg'.format(pesoMenor))



