#Calcular Média de Valores em uma Lista

from typing import List

def media(lista: List[float])-> float:
    resultado = sum(lista)/len(lista)
    return resultado

lista_1 = [2,3,5,10]
print(media(lista_1))









