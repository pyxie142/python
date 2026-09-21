testes = [
    "[a + b] * [c - d]",
    "[[a + b]",
    "[a + b]]",
    "a + b",
    "]["
]
for expressao in testes:
    pilha = []
    valida = True
    for caractere in expressao:
        if caractere == '[':
            pilha.append(caractere)
        elif caractere == ']':
            if len(pilha) == 0:
                valida = False
            else:
                pilha.pop()
    if len(pilha) != 0:
        valida = False
    if valida == True:
        resultado = "Correta"
    else:
        resultado = "Incorreta"
    print("Expressão:", expressao, "->", resultado)
