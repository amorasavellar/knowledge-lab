# Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def soma_numeros(lista):
    total=0
    for numero in lista:
        total += numero
    return total

lista = [10,5,20,5]

print(soma_numeros(lista))