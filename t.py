n = 0
c = 0
m = 1
while n != 757:
    n = int(input('Digite um número [757 para parar]: '))
    c += 1
    m *= n
print(f'Você digitou {c} números e a multiplicação entre eles foi {m}')
