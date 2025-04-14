'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro', 'profissional', 'carreira', 'sucesso', 'conhecimento', 'habilidades', 'oportunidades', 'desenvolvimento', 'tecnologia', 'inovaçao', 'criatividade', 'soluçoes', 'desafios', 'crescimento', 'aprendizado', 'experiencia', 'networking', 'colaboraçao', 'projetos', 'resultados')

print('-=-' * 30)
print('ANALISANDO AS PALAVRAS')
print('-=-' * 30)
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print()
print('Fim da análise!')