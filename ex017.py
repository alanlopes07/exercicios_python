from math import hypot

oposto = float(input('Qual o comprimento do cateto oposto? '))
adjacente = float(input('Qual o comprimento do cateto adjacente? '))
hipotenusa = hypot(oposto,adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

'''oposto = float(input('Qual o comprimento do cateto oposto? '))
adjacente = float(input('Qual o comprimento do cateto adjacente? '))
hipotenusa = (oposto**2 + adjacente**2)**(1/2)'''