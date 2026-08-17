brasileirao = [
    "Palmeiras", "Flamengo", "Athletico-PR", "Fluminense", "Red Bull Bragantino", 
    "Bahia", "Botafogo", "Atlético-MG", "Corinthians", "Coritiba", 
    "Cruzeiro", "São Paulo", "Vitória", "Santos", "Gremio", 
    "Internacional", "Vasco da Gama", "Clube do Remo", "Mirassol", "Chapecoense"
]

# 1. Busca os 5 primeiros (índices 0 a 4)
print(f'Os 5 primeiros classificados do brasileirão são: {brasileirao[0:5]}')

# 2. Busca os 4 últimos (índices -4 até o final)
print(f'Os 4 últimos classificados do brasileirão são: {brasileirao[-4:]}')

# 3. Ordena a lista temporariamente em ordem alfabética
print(f'Times em ordem alfabética: {sorted(brasileirao)}')

# 4. Encontra o índice da Chapecoense e soma 1 para a posição real
print(f'A Chapecoense está na {brasileirao.index("Chapecoense") + 1}º posição')
