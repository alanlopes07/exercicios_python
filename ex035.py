print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2: 
  print('Os segmentos {}, {} e {} podem formar um triângulo!'.format(s1,s2,s3))
else: 
  print('Os segmentos {}, {} e {} não podem formar um triângulo.'.format(s1,s2, s3))