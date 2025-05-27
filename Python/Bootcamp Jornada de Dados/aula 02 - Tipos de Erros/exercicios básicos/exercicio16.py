# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
primeira_expressao = bool(input("Digite a primeira expressão Falsa ou Verdadeira: "))
segunda_expressao = bool(input("Digite a segunda expressão Falsa ou Verdadeira: "))

result = primeira_expressao and segunda_expressao

print(f"O resultado das expressões inseridas é: {result}")