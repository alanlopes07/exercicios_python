#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

totalMaior = 0
totalMenor = 0
for pess in range(1,8):
  ano = int(input('Informe o ano que a {}ª pessoa nasceu: '.format(pess)))
  idade = date.today().year - ano
  if idade >= 21:
    totalMaior +=1
  else:
    totalMenor +=1
print('O número total de pessoas maiores de idade é de: {}'.format(totalMaior))
print('Também tivemos {} pessoas menor de idade.'.format(totalMenor))

    
