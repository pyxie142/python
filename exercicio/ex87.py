impar = []
par = []

for c in range(0, 7):
    # Lê o número diretamente em uma variável
    valor = int(input(f'Digite o {c+1}º valor: '))
    
    # Adiciona o número diretamente (como inteiro, não como lista)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

# Ordena as listas de números
par.sort()
impar.sort()

print(f'Os valores pares em ordem crescente foram {par} e os ímpares {impar}')
