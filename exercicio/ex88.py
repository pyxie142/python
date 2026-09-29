# Inicializa uma matriz 3x3 com zeros
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Laço para preencher a matriz com dados do usuário
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

# Laço para exibir a matriz formatada na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
