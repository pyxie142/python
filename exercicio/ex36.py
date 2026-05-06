salario = float(input("Qual é o salário do funcionário? R$ "))
aumento15 = salario + (salario*0.15)
aumento10 = salario + (salario*0.10)
if salario > 1250:
    print("Quem ganhava {} passa a ganhar {}".format(salario,aumento10))
else:
        print("Quem ganhava {} passa a ganhar {}".format(salario,aumento15))