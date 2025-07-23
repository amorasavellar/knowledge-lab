#Contar Valores Únicos em uma Lista

def valores_unicos(valores: List[float]) -> List[float]:
    lista = list(set(valores))
    return lista

lista_3 = [1,2,3,3,4,5]
print(valores_unicos(lista_3))