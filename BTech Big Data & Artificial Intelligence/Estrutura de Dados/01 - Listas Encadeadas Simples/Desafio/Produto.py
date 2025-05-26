  
# Criação de Classes

#classe Produto
class Produto:
    def __init__(self, Codigo = "Indefinido", Peso=0):
        self.Codigo = Codigo
        self.Tipo = Peso
    
    def __repr__(self):
        return '%s -> %d' % (self.Codigo, self.Tipo)
        
    
                
