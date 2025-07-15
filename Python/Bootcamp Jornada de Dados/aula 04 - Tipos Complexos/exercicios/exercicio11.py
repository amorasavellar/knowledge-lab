# Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {'nome': 'Notebook', 'preco': 2500},
    {'nome': 'Smartphone', 'preco': 1500},
    {'nome': 'Tablet', 'preco': 800}
]

for produto in produtos:
    if produto['nome'] == 'Smartphone':
        produto['preco'] = 90
        
print("Produtos atualizados:", produtos)