# Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict_fundido = {**dict1, **dict2}
print("Dicionário fundido:", dict_fundido)