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

teste = []
teste.append('pietra')
teste.append(30)
galera = []
#galera.append(teste)
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
#galera.append(teste) muda a lista de cima pois eu estou ligando as listas
galera.append(teste[:]) #agora ele ta fazendo uma copia e não ligando as listas
print(teste)
print(galera)
