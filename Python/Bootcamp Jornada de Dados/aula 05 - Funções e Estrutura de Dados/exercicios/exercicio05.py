# Calcular Desvio Padrão de uma Lista

def desvio_padrao(valores: List[float]) -> float:
    media = sum(valores)/len(valores)
    varianca = sum((x-media)**2 for x in valores)/len(valores)
    desvio = varianca **0.5
    return desvio

lista_4 = [2,4,5,6,7]
print(desvio_padrao(lista_4))