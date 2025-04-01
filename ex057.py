#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo da pessoa: [M/F] ').strip().upper()[0])

while sexo not in ('F', 'M'):
  sexo = str(input('Entrada não valida, por favor digite o sexo da pessoa: [M/F] ').upper()[0])
if sexo == 'F':
 sexo = 'Feminino'
if sexo == 'M':
 sexo = 'Masculino'
print('O sexo {} foi registrado com sucesso!'.format(sexo))