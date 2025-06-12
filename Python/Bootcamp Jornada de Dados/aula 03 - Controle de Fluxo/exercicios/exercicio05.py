# Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# transações suspeitas. Uma transação é considerada suspeita se o valor for
# superior a R$ 10.000 ou se ocorrer fora do horário comercial
# (antes das 9h ou depois das 18h). Dada uma transação como
# transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}
cond = [0,0]

if transacao['hora'] <9 or transacao['hora'] >18:
    cond[0] = 1
if transacao['valor'] > 10000:
    cond[1] = 1

#avaliação
if cond[0] and cond[1]:
    print("Transação Suspeita")
else:
    print("Transação Normal")