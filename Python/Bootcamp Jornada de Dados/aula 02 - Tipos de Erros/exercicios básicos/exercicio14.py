# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = str(input("Digite uma data no formato dd/mm/aaaa: "))

dia, mes, ano = data[0:2], data[3:5], data[6:10]


print(f"Dia {dia}, Mês {mes}, Ano {ano}")