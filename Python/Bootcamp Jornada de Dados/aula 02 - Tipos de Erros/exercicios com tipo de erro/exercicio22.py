# Crie um programa que verifica se uma palavra ou frase é um palíndromo
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
# Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize
# a função isinstance() para verificar o tipo da entrada.

palavra = input("Digite uma palavra ou frase: ")

if isinstance(palavra, str):
    palavra_formatada = palavra.replace(" ", "").lower()
    if palavra_formatada == palavra_formatada[::-1]:
        print("Essa palavra é um palíndromo.")
    else:
        print("Essa palavra não é um palíndromo.")    
else:
    print("Entrada digitada fora do formato, por favor digite novamente.")