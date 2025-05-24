# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temperatura = float(input("Digite uma temperatura em graus Celsius (Ex: 35.7): "))

conversao = (temperatura * 9//5) + 32

print(f"A temperatura {temperatura}C em Fahrenheit é {conversao}")