nome = input ("qual seu nome?")
print ("prazer em conhece-lo{:20}!" .format(nome))
print ("prazer em conhece-lo{:>20}!" .format(nome))
print ("prazer em conhece-lo{:<20}!" .format(nome))
print ("prazer em conhece-lo{:^20}!" .format(nome))
nu = int (input("digite um valor "))
nu2 = int (input("digte outro valor "))
soma = (nu+nu2) # criar variavel quando ultilizar em outra parte do codigo
print ("a soma é {}" .format(soma))