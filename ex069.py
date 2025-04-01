'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
tot18 = m = f20 = 0  
while True: 
  print('=-=' * 30)
  idade = int(input('Idade: '))
  sexo = ' '
  while sexo not in 'MF':
    print('=-=' * 30)
    sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
  if idade > 18:
    tot18 +=1
  if sexo == 'm' or sexo == 'M':
    m += 1
  if idade < 20 and sexo == 'F':
    f20 +=1
  mantem = ' '
  while mantem not in 'SN':
   print('=-=' * 30)
   mantem = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if mantem == 'n' or mantem == 'N':   
    print(f'O total de pessoas com mais de 18 anos foi {tot18}, foram cadastrados {m} homens, tambem tivemos {f20} mulheres com menos de 20 anos.')
    break
    