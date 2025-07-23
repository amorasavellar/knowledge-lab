# Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

print(numero_primo(7))  # True
print(numero_primo(10)) # False