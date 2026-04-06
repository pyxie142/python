frase = ('curso de análise e desenvolvimento de sistemas')
print(frase[3]) #isso mostra o espaço da memória
print(frase[3:46]) #intervalo de caracteres menos o último
print(frase[3:45:2]) #pula de dois em dois
print(frase[:9]) #do inicio ate o caractere que escolhi
print(frase[9:]) #do caractere que escolhi até o final
print(frase[9::3]) #pega do caractere que eu escolhi pulando de 3 em 3
print(len(frase)) #esse metodo conta a quantidade de caracteres
print(frase.count('t')) #procura caractere especifico na variavel
print(frase.count('a',6,7)) #procura caractere especifico dentro de um intervalo especifico
print(frase.find('sis')) #mostra a partir de qual indice aparece a pesquisa 
print(frase.find('android')) #o resultado -1 indica que nn tem essa sequencia na variavel
print('amo' in frase) #o in verifica se aquele conjunto de string esta na variavel