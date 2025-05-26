class Bagagem:
    def __init__(self, Codigo="indefinido", Peso=0):
        self.Codigo = Codigo
        self.Peso = Peso
    
    def __repr__(self):
        return '%s -> %d' %(self.Codigo, self.Peso)