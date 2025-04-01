'''n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
maior_valor = max(n1, n2, n3)
menor_valor = min(n1, n2, n3)

print('O menor valor digitado foi {}'.format(menor_valor))
print('O maior valor digitado foi {}'.format(maior_valor))'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a 
if b<a and b<c:
  menor = b
if c<a and c<b:
  menor = c
print('O menor valor digitado foi {}'.format(menor))

maior = a 
if b>a and b>c:
  maior = b
if c>a and c>b:
  maior = c
print('O maior valor digitado foi {}'.format(maior))
