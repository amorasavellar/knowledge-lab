# Contar ocorrências de caracteres

texto = "Egenharia de Dados é uma área fascinante!"

def conta_caracteres(texto):
    contagem = {}
    for letra in texto:
        contagem[letra] = contagem.get(letra, 0) + 1
    return contagem

print(conta_caracteres(texto))
    