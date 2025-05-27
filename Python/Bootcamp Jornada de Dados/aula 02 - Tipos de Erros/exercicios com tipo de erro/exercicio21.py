# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# 1 - Solicitar ao usuario a temperatura em Celsius
# 2 - Garantir que o valor de entrada seja numerico
# 3 - Converter a temperatura para Fahrenheit
# 4 - Imprimir resultado

try:
    temp_celsius = float(input("Digite uma temperatura em Celsius (Ex: 32.3): "))
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f"A temperatura {temp_celsius}C convertida em Fahrenheit é: {temp_fahrenheit}F")
except ValueError:
    print("Valor digitado fora do formato, por favor digite novamente.")