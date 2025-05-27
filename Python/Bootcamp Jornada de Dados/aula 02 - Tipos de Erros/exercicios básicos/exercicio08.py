# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero = float(input("Digite um número decimal (Ex: 1.20): "))
expoente = int(input("Digite um número inteiro para ser usado como expoente (Ex: 2): "))

potencia = numero ** expoente

print(f"O resultado do número {numero} elevado pela potencia {expoente}, é: {potencia}")
