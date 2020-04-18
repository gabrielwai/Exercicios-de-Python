tabela_brasileirao = ('Atlhetico-PR','Athletico-GO','Athletico-MG','Bahia','Botafogo',
                      'Bragantino','Ceará','Corinthians','Coritiba','Flamengo','Fluminense',
                      'Fortaleza','Goiás','Grêmio','Internacional','Palmeiras','Santos',
                      'São Paulo','Sport','Vasco')
print('-=-'*10, end=' Campeonato Brasileirão ')
print('-=-'*10)
#print(len(tabela_brasileirao))
print(f'\nTimes de acordo com sua classificação: {tabela_brasileirao}')
print(f'\nOs primeiros 5 colocados são: {tabela_brasileirao[:5]}', end=f'\n\nOs 5 últimos são: {tabela_brasileirao[(len(tabela_brasileirao)-5):]}')

if 'Chapecoense' in tabela_brasileirao:
    print(f'\n\nA Chapecoense está na {tabela_brasileirao.index("Chapecoense")+1}ª posição', end='')

print(f'\n\nOs times em ordem alfabética são: {sorted(tabela_brasileirao)}')
#print('Chapecoense' in tabela_brasileirao)
