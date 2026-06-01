preco_normal = float(input("Digite o preço normal do produto: R$ "))
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque (15% de desconto)
[2] À vista no cartão (8% de desconto)
[3] Em até 2x no cartão (Preço normal)
[4] Em 3x ou mais no cartão (25% de juros)''')
opcao = int(input("Qual é a opção de pagamento? "))
if opcao == 1:
    total = preco_normal * 0.85
    print(f"Sua compra de R$ {preco_normal:.2f} vai custar R$ {total:.2f} à vista.")
elif opcao == 2:
    total = preco_normal * 0.92
    print(f"Sua compra de R$ {preco_normal:.2f} vai custar R$ {total:.2f} no cartão à vista.")
elif opcao == 3:
    total = preco_normal
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.")
    print(f"Sua compra vai custar o preço normal de R$ {total:.2f}.")
elif opcao == 4:
    total = preco_normal * 1.25
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = total / total_parcelas
    print(f"Sua compra será parcelada em {total_parcelas}x de R$ {parcela:.2f} COM JUROS.")
    print(f"Sua compra de R$ {preco_normal:.2f} vai custar R$ {total:.2f} no final.")
else:
    print("Opção inválida de pagamento. Tente novamente!")
