from lista_encadeada import ListaEncadeada
from bagagem import Bagagem
from nodo import Nodo

lista = ListaEncadeada()

lista.NovaBagagem(Bagagem("001", 10))
lista.NovaBagagem(Bagagem("002", 15))
lista.NovaBagagem(Bagagem("003", 25))
lista.NovaBagagem(Bagagem("004", 20))
lista.NovaBagagem(Bagagem("005", 30))

lista.ImprimeLista()

print("Peso total: ",lista.PesoTotal())