from random import randint
print('Vamos jogar par ou ímpar')
cont = 0
while True:
    palpite = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? ')).strip().lower()
    pc = randint(1, 10)
    resultado = palpite + pc
    venceu_par = (resultado % 2 == 0 and escolha == 'par')
    venceu_impar = (resultado % 2 != 0 and escolha == 'impar')
    
    if venceu_par or venceu_impar:
        print(f'Você jogou {palpite} e o computador jogou {pc}. Total deu {resultado} ({escolha.upper()})')
        cont += 1
        print('Você VENCEU!')
    else:
        escolhapc = 'par' if resultado % 2 == 0 else 'impar'
        print(f'Você jogou {palpite} e o computador jogou {pc}. Total deu {resultado} ({escolhapc.upper()})')
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente ...\n')
print(f'Game Over! Você venceu {cont} vezes.')
