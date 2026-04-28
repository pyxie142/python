#Condições (exemplo)
#tempo = int(input("Quantos anos tem seu carro?"))
#if tempo<=3:
#    print('carro novo')
#else:
#    print('carro velho')
#print('--fim--')
#Condições simplicaficada (exemplo)
#tempo = int(input("Quantos anos tem seu carro?"))
#print('carro novo' if tempo<=3 else'carro velho')
#print('--fim--')
#nome = str(input('Qual é o seu nome?'))
#if nome == 'pietra':
#    print('Que nome lindo você tem!')
#else:
#    print('seu nome é tão normal')
#print('Bom dia {}!'.format(nome))
#Condições simplicaficada (exemplo)
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m=(n1 + n2)/2
print("A sua média foi {:.1f}".format(m)) 
if m >= 6.0: 
    print("A sua média foi boa! Parabéns")
else: 
    print("Sua média foi ruim! Estude mais")
print("Parabéns" if m >= 6 else "Estude mais")