# Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

def chaves_ordenadas(dicionario):
    """
    Recebe um dicionário e retorna uma lista de suas chaves ordenadas.
    
    :param dicionario: dict - O dicionário cujas chaves serão ordenadas.
    :return: list - Lista de chaves ordenadas do dicionário.
    """
    return sorted(dicionario.keys())

print(chaves_ordenadas({'banana': 1, 'maçã': 2, 'laranja': 3}))  # Deve retornar ['banana', 'laranja', 'maçã']