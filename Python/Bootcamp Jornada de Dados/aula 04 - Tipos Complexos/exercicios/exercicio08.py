# Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {'nome': 'Ana', 'idade': 30},
    {'nome': 'Carlos', 'idade': 25},
    {'nome': 'Bruno', 'idade': 22}
]
pessoas.sort(key=lambda pessoa: pessoa['nome'])
print(f"Pessoas ordenadas por nome: {pessoas}")
pessoas.sort(key=lambda pessoa: pessoa['idade'])
print(f"Pessoas ordenadas por idade: {pessoas}")