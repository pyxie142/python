# materias=[]
# quimica=[]
# back=[]
# materias.append(quimica[:])
# materias.append(back)
# [[quimica,back]]
# pessoas=[['pedro',75], ['maria',19]]
# print(pessoas[0][0]) = pedro
# print(pessoas[1][1]) = 19


# print(pessoas[1][0]) = maria 
# print(pessoas[0]) = pedro,75

# teste = []
# teste.append('pietra')
# teste.append(30)
# galera = []
# #galera.append(teste)
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# #galera.append(teste) muda a lista de cima pois eu estou ligando as listas
# galera.append(teste[:]) #agora ele ta fazendo uma copia e não ligando as listas
# print(teste)
# print(galera)

# galera=[['joao',19], ['ana',33],['joaquim',17],['maria',49]]
# print(galera[2][1])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

galera=[]
dado=[]
tomai=tomen=0
for c in range (0,3):
    dado.append(str(input('nome')))
    dado.append(int(input('idade')))
    galera.append(dado[:])
    dado.clear()
print(galera)
