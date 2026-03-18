dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos km foram percorridos? "))
precodias = dias * 60
precokm = km * 0.15
total = precodias + precokm
print("O total a pagar pelo aluguel é: R$ {:.2f}" .format(total))