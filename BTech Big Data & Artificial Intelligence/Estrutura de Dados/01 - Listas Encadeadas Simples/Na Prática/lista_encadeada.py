class ListaEncadeada:
    
    def __init__(self):
        self.inicio = None
    
    def __repr__(self):
        return "[" + str(self.inicio) + "]"
    
    def ListaVazia(self):
        if self.inicio == None:
            return True
        else:
            return False
        
    def ImprimeLista(self):
        
        atual = self.inicio
        cont=0
        print("Inicio da Lista")
        
        if self.inicio == None:
            print("Lista Vazia")
        else:
            while atual!= None:
                print("Posição: ", cont, atual)
                cont = cont+1
                atual = atual.proximo
        print("Final da Lista")
        
    def NovaBagagem(self, Nd):
        
        #Cria o nodo com 1 elemento da lista
        atual = self.inicio
        #Atribui ao novo nodo o primeiro elemento da lista
        Nd.proximo = atual
        #Atualiza o primeiro elemento da lista como sendo o novo elemento
        self.inicio = Nd
        
    def PesoTotal(self):
        
        atual = self.inicio
        peso = 0
        
        if self.inicio == None:
            return 0
        else:
            while atual!= None:
                peso = peso + atual.Peso
                atual = atual.proximo
                
        return peso