#Filtrar Dados Acima de um Limite

def filtra_acima_de(valores: List[float], limite:float) -> List[float]:
    lista = [item for item in valores if item >= limite]
    return lista

lista_2 = [10,20,30,40,50]
print(filtra_acima_de(lista_2, limite=20))