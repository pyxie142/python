largura = float(input('Largura da parede (m): '))
altura = float(input('Altura da parede (m): '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')
