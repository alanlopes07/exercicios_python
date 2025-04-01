#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('=' * 20)
print('10 TERMOS de uma PA')
print('=' * 20)

n = int(input('Digite o primeiro termo: '))
r = int(input('Razao: '))
termo = n
cont = 1 
total = 0
mais = 10
while mais != 0:
  total = total + mais
  while cont <= total:
    print('{} --> '.format(termo), end = '')
    termo += r
    cont += 1 
  print('PAUSA')
  mais = int(input('Quantos termos você quer mostrar a mais ? ')) 
print('FIM')
print('Progressão finalizada com {} termos mostrados.' .format(total))