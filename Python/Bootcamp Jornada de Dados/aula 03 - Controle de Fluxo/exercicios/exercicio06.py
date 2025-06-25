# Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto="O rato roeu a roupa do rei de Roma"

palavras = texto.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra]+=1
    else:
        contagem[palavra] =1
print(contagem)