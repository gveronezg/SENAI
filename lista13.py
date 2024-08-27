# Lista13.1. Crie um dicionário vazio.
dic = {}

# Lista13.2. Crie um dicionário com 3 pares chave-valor de strings.
dic = {'a':'letraA','b':'letraB','c':'letraC'}

# Lista13.3. Acesse o valor de uma chave específica em um dicionário.
dic = {'a':'letraA','b':'letraB','c':'letraC'}
print(dic['a'])

# Lista13.4. Adicione um novo par chave-valor a um dicionário.
dic = {'a':'letraA','b':'letraB','c':'letraC'}
print(dic)
dic['d'] = 'letraD'
print(dic)

# Lista13.5. Remova um par chave-valor de um dicionário usando a função pop.
dic = {'a':'letraA','b':'letraB','c':'letraC'}
print(dic)
dic.pop('b','ruim')
print(dic)

# Lista13.6. Verifique se uma chave específica está presente em um dicionário.
dic = {'a':'letraA','b':'letraB','c':'letraC'}
letra = input(str('Entre com uma letra: '))
if letra in dic:
    print(f'{letra} está em dic!')
else:
    print(f'{letra} não está em dic!')

# Lista13.7. Verifique se um valor específico está presente em um dicionário.
dic = {'a':'letraA','b':'letraB','c':'letraC'}
valor = input(str('Entre com um valor: '))
if valor in dic.values():
    print(f'{valor} está em dic!')
else:
    print(f'{valor} não está em dic!')

# Lista13.8. Conte quantos pares chave-valor um dicionário possui.
dic = {'a':'letraA','b':'letraB','c':'letraC'}
cont = 0
for qtd in dic:
    cont += 1
print(f'Existem {cont} pares no dicionário...')
print(dic)

# Lista13.9. Copie um dicionário para outro.
dic = {'a':'letraA','b':'letraB','c':'letraC'}
print(dic)
vazio = {}
print(vazio)
for par in dic:
    vazio[par] = dic[par]
print(vazio)

# Lista13.10. Limpe todos os itens de um dicionário.
dic = {'a':'letraA','b':'letraB','c':'letraC'}
print(dic)
dic.clear()
print(dic)

# Lista13.11. Crie um dicionário com tipos de frutas e seus respectivos preços.
frutas = [
    {'nome':'maçã','tipo':'doce','preço':1.0},
    {'nome':'limão','tipo':'azedo','preço':0.5}
]
print(frutas)

# Lista13.12. Atualize o valor de uma chave específica em um dicionário.
dados = {'nome':'Gabriel','ocupação':'Desenvolvedor'}
print(dados)
dados['ocupação'] = 'Analista'
print(dados)

# Lista13.13. Junte dois dicionários usando o método update.
fruta = {'nome':'maçã','tipo':'doce'}
print(fruta)
update = {'preço':0.5,'cor':'vermelha'}
fruta.update(update)
print(fruta)

# Lista13.14. Acesse todas as chaves de um dicionário usando o método `keys`.
fruta = {'nome': 'maçã', 'tipo': 'doce', 'preço': 0.5, 'cor': 'vermelha'}
chaves = list(fruta.keys())
print(chaves)

# Lista13.15. Crie um dicionário com informações sobre rios (nome, extensão, país de origem, etc.).
rios = [
    {'nome':'Rio Amazonas','extensão':'6.400km','páis':'Brasil'},
    {'nome':'Rio São Francisco','extensão':'2.830km','páis':'Brasil'},
    {'nome':'Rio Paraná','extensão':'4.880km','páis':'Brasil'},
]
print(rios)

# Lista13.16. Crie um dicionário com informações sobre oceanos (nome, área, profundidade média, etc.).

# Lista13.17. Crie um dicionário com informações sobre esportes (nome, modalidades, país de origem, etc.).

# Lista13.18. Crie um dicionário com informações sobre artistas de cinema (nome, filmes famosos, prêmios recebidos, etc.).

# Lista13.19. Crie um dicionário com informações sobre marcas de roupas (nome, país de origem, estilo, etc.).