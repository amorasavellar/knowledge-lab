# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
primeira_expressao = bool(input("Digite a primeira expressão Falsa ou Verdadeira: "))
segunda_expressao = bool(input("Digite a segunda expressão Falsa ou Verdadeira: "))

result = primeira_expressao or segunda_expressao

print(f"O resultado das expressões inseridas é: {result}")