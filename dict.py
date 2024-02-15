produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
precos = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]
quantidade_vendas = [20, 30, 50, 69, 80, 70, 110, 6500, 25, 35]

lista_produtos_dados = []

for i,venda in enumerate(quantidade_vendas):
    lista2 = [precos[i], venda]
    lista_produtos_dados.append(lista2)


produtos_dados = zip(produtos, lista_produtos_dados)

dicionario_de_produtos_com_dados = dict(produtos_dados)

for produto in dicionario_de_produtos_com_dados:
    valor, quantidade = dicionario_de_produtos_com_dados[produto]
    print('O produto {} com o preço R$ {:,} vendeu {} unidades'.format(produto, valor, quantidade))
    valor_total = valor * quantidade
    print('Valor total do produto {} em estoque: R$ {:,}'.format(produto, valor_total))
    print('-------------------------------------------------------')