n = int(input('Quantos termos você quer mostrar? '))
t1 = 0  # Primeiro termo
t2 = 1  # Segundo termo

print(f'{t1} -> {t2}', end='')
cont = 3  # Contador começa no 3º termo

while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    
    # Faz a sequência avançar
    t1 = t2
    t2 = t3
    cont += 1

print(' -> FIM')
