# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos
# e tenha fornecido um email válido. Escreva um programa que valide essas
# condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = 18
email = 'user@exemple.com'
cond = [0,0]

if idade >=18 and idade <=65:
    cond[0] = 1
if "@" in email and ".com" in email:
    cond[1] = 1

#avaliacao
if cond[0] and cond[1]:
    print("Dados de usuário validos")
else:
    print("Dados de usuário invalidos")