# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = str(input("Insira uma frase (Ex: O rato roeu a roupa do rei de Roma): "))

print(f"A frase digitada sem espaço no inicio e no fim é: {frase.strip()}")