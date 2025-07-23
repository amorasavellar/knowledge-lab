#Encontrar Valores Ausentes em uma Sequência

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

lista_5 = [1,2,3,7]
print(encontrar_valores_ausentes(lista_5))