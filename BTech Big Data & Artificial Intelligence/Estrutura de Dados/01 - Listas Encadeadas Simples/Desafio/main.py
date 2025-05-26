#programa principal

#importando classes criadas
from ListaEncadeada import ListaEncadeada
from Produto import Produto
from Nodo import Nodo


#Declaração da lista vazia
lista = ListaEncadeada()

#Criação dos nodos do Tipo Bagagem e dadionados na lista
lista.NovoProduto(Produto("001",1))
lista.NovoProduto(Produto("002",0))
lista.NovoProduto(Produto("003",1))
lista.NovoProduto(Produto("004",0))
lista.NovoProduto(Produto("005",0))

#Chamada do método de impressão da lista desenvolvido para verificação se for realizado como previsto
lista.ImprimeLista()

#Impressão do total de produtos que precisam de refrigeração
lista.TotalProdutoRefrigerado()