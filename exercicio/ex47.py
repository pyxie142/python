from random import randint
from time import sleep
print('''Suas opções
[0] pedra
[1] papel
[2] Tesoura''')
jogada = int(input("Qual é a sua jogada?"))
jogadapcc= randint(0,2)
Itens = ("Pedra", "Papel", "Tesoura")
print("jo")
sleep(1)
print("ken")
sleep(1)
print("po !!!")
sleep(1)
print("-=-" * 10)
print(f'''computador jogou {Itens[jogadapcc]}
jogador jogou {Itens [jogada]}''')
print("-=-" * 10)
if jogadapcc == 0 and jogada == 2 or jogadapcc == 1 and jogada or jogadapcc ==2 and jogada == 1:
    print("Computador vence")
elif jogada == 0 and jogadapcc == 2 or jogada == 1 and jogadapcc == 0 or jogada == 2 and jogadapcc == 3:
    print("Jogador vence")
else:
    print("empate")