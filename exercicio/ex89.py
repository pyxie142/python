# Inicialização da matriz 3x3 e das variáveis de controle
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
total3 = maior = somapar = 0

# Leitura dos dados e processamento dos valores
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
        # 1. Soma dos valores pares
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
            
        # 2. Soma dos valores da terceira coluna (índice 2)
        if c == 2:
            total3 += matriz[l][c]
            
        # 3. Maior valor da segunda linha (índice 1)
        if l == 1 and c == 0:
            maior = matriz[l][c]
        elif l == 1 and c != 0 and matriz[l][c] > maior:
            maior = matriz[l][c]

print('-=' * 30)

# Exibição da matriz formatada na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 30)

# Exibição dos resultados das análises
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos números da terceira coluna é igual a {total3}.')
print(f'O maior valor da linha 2 é {maior}.')
