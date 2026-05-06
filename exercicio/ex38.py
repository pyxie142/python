casa = float (input("qual o valor da casa? "))
salario = float(input("Salario do comprador: R$"))
Finaciamento = int(input("Quantos anos de financiamento?"))
prestacao = casa / (Finaciamento * 12) 
if prestacao <= salario*0.3:
    print("Para pagar uma casa de {} em {} anos a prestação será de R$ {} é suficiente. Emprestimo aprovado".format(casa, Finaciamento, prestacao))
elif prestacao > salario * 0.3:
    print("Para pagar uma casa de {} em {} anos a prestação será de R$ {} é muito pouco. Emprestimo negado".format (casa, Finaciamento, prestacao))