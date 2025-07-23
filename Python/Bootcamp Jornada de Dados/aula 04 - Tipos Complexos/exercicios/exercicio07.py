# Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades = [15, 22, 17, 19, 30, 12, 25]
idades_maiores_18 = [idade for idade in idades if idade >= 18]
print("Idades maiores ou iguais a 18:", idades_maiores_18)