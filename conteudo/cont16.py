# pessoas = {'nome':'pietra','sexo':'f','idade':18}
# print(pessoas['nome'])
# print(f'a {pessoas['nome']} tem {pessoas['idade']} anos')
# print(pessoas.keys())
# print(pessoas.items())

# Brasil=[]
# Estado1={'uf':'Rio de Janeiro','sigla':'rj'}
# Estado2={'uf':'São Paulo', 'sigla':'sp'}
# Brasil.append(Estado1)
# Brasil.append(Estado2)
# print(Estado1)
# print(Brasil)
# print(Brasil[0])
# print(Brasil[1])
# print(Brasil[0]['uf'])
# print(Brasil[1]['sigla'])

Estado={}
Brasil=[]
for c in range(0,3):
        Estado['uf']=str(input('unidade federativa'))