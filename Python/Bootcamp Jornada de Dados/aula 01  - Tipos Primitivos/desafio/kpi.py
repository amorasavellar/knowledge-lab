CONSTANTE_BONUS = 1000

# 1) Solicite ao usuario que digite seu nome
name = str(input("Digite seu nome (Ex: Leandro): "))

# 2) Solicete ao usuario que digite o valor do seu salario
# (Converta o valor de entrada para float)
salario = float(input("Digite o valor do seu salario (Ex: 1000): "))

# 3) Solicite ao usuario que digite a porcentagem do bonus recebido
# (Converta o valor de entrada para float)
bonus = float(input("Digite a porcentagem do seu bonus (Ex: 2.5): "))

# 4) Calcule o valor do bonus final
kpi = CONSTANTE_BONUS + salario * bonus

# 5) Imprima o valor do KPI para o usuario
print(kpi)

# 6) Imprima uma mensagem personalizada incluindo o nome, salario e bonus do usuario
print(f"Olá {name}, o seu bonus foi de {kpi}")

# Bonus: Quantos bugs voce vai identificar nesse programa?