print('-=-' * 20)
print('Irei analisar para você se o número informado é par ou ímpar.')
print('-=-' * 20)
numero = int(input('Informe um número: '))
if numero % 2 == 0:
    print('O numero {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))