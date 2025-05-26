#Classe Nodo
class Nodo:
    class Nodo:
        def __init__(self, dado=0, proximo_nodo=None):
            self.conteudo = dado
            self.proximo = proximo_nodo
            
    def __repr__(self):
        return '%s -> %s' % (self.conteudo, self.proximo)