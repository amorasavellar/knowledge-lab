# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
primeiro_numero = int(input("Digite o primeiro número inteiro (Ex: 1): "))
segundo_numero = int(input("Digite o segundo número inteiro (Ex: 1): "))

comparacao = primeiro_numero != segundo_numero

print(f"Os dois números são diferentes? {comparacao}")