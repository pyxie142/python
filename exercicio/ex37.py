print("---" * 10)
print("Analisador de triângulos")
print("---" * 10)
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("As retas podem formar um triângulo.")
else:
    print("As retas NÃO podem formar um triângulo.")