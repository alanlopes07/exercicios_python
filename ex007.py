n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print('A média entre {} e {} é igual a {:.1f}'.format(n1, n2, media))

if media >= 7:
    print('Parabéns, você foi aprovado!')

else:
    print('Você foi reprovado, estude mais!')