CONSTANTE_BONUS = 1000

# 1) Solicite ao usuario que digite seu nome
try:
    name = str(input("Digite seu nome (Ex: Leandro): "))

    if name.isdigit():
        print("Você digitou seu nome errado, Por favor digite seu nome")
        exit()
    elif len(name)==0:
        print("Você não digitou seu nome, Por favor digite seu nome")
        exit()
    elif name.isspace():
        print("Você digitou espaço, Por favor digite seu nome")
        exit()
except ValueError:
    print("Você digitou um valor inválido")
    
# 2) Solicete ao usuario que digite o valor do seu salario
# (Converta o valor de entrada para float)
try:
    salario = float(input("Digite o valor do seu salario (Ex: 1000): "))

    # Salrio menor negativo ou zero
    if salario <= 0:
        print("Você digitou um salario menor ou igual a zero")
        exit()
except ValueError:
    print("Você digitou um valor inválido")

# 3) Solicite ao usuario que digite a porcentagem do bonus recebido
# (Converta o valor de entrada para float)
try:
    bonus = float(input("Digite a porcentagem do seu bonus (Ex: 2.5): "))

    # bonus negativo ou igual a zero
    if bonus <= 0:
        print("Você digitou um bonus menor ou igual a zero")
        exit()
except ValueError:
    print("Você digitou um valor inválido")

# 4) Calcule o valor do bonus final
kpi = CONSTANTE_BONUS + salario * bonus

# 5) Imprima o valor do KPI para o usuario
#print(kpi)

# 6) Imprima uma mensagem personalizada incluindo o nome, salario e bonus do usuario
print(f"Olá {name}, o seu bonus foi de R$ {kpi:.2f}")

# Bonus: Quantos bugs voce vai identificar nesse programa?