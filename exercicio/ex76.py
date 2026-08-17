from random import randint

# Gera uma tupla com 5 números aleatórios entre 1 e 10
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) #variável composta

print(f'Eu sorteei os valores {n}')
print(f'O maior valor foi {max(n)}') #método de tuplas
print(f'O menor valor foi {min(n)}') #método de tuplas
