'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0



while opcao != 5:
  print('=-=' * 20)
  print('[ 1 ] Soma\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa')
  print('=-=' * 20)
  opcao = int(input('Qual ação deseja realizar? '))
  sleep(1)
  print('=-=' * 20)

  if opcao > 5 or opcao < 1:
      print('Opção inválida, tente novamente!')

  if opcao == 1: 
      soma = n1 + n2
      print('A soma entre os números é {}'.format(soma))
  elif opcao == 2:
      multiplica = n1 * n2
      print('A multiplicação entre os números é {}'.format(multiplica))
  elif opcao == 3:
    if n1 > n2:
        print('{} é maior que {} '.format(n1, n2))
    elif n2 > n1:
        print('{} é maior que {}'.format(n2, n1))
    else:
        print('{} e {} são iguais'.format(n1, n2))
  elif opcao == 4:
      n1 = int(input('Primeiro valor: '))
      n2 = int(input('Segundo valor: '))

print('Saindo do programa...')
sleep(1)
print('Volte sempre!')