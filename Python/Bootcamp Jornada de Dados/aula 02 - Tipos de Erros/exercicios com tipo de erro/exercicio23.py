# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador
# (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas
# não numéricas. Utilize if-elif-else para realizar a operação matemática baseada
# no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    primiero_numero = float(input("Digite um número: "))
    operador = float(input("Digite o operador desejado (+, -, *, /): "))
    segundo_numero = input("Digite outro número: ")

    if operador == "+":
        resultado = primiero_numero + segundo_numero
    elif operador == "-":
        resultado = primiero_numero - segundo_numero
    elif operador == "*":
        resultado = primiero_numero * segundo_numero
    elif operador == "/" and segundo_numero !=0:
        resultado = primiero_numero / segundo_numero
    else:
        print("Divisão por zero, operador invalido.")
    print(f"Resultado: {resultado}")
except ValueError:
    print("Entrada Invalida. Insira os números corretamente.")