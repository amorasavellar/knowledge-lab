# Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

def encontrar_pares(lista, numero):
    pares = []
    vistos = set()
    
    for num in lista:
        complemento = numero - num
        if complemento in vistos:
            pares.append((complemento, num))
        vistos.add(num)
    
    return pares

print(encontrar_pares([1, 2, 3, 4, 5], 5))  # Exemplo de uso: deve retornar [(2, 3), (1, 4)]
print(encontrar_pares([10, 15, 3, 7], 17))  # Exemplo de uso: deve retornar [(10, 7), (15,2)]