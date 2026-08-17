


from random import randint

print('sou seu computador')
print('''acabei de pensar em um número entre 0 e 9
será que você consegue adivinhar qual foi?''')

palpite = int(input('qual é o seu palpite? '))
aleatorio = randint(0, 9)

if palpite == aleatorio:
    print('você ganhou e o computador perdeu!')
else:
    print(f'o computador ganhou! ele pensou no número {aleatorio}')
