#classe Lista Encadeada
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
        
    # O método de impressão percorre toda a slita até o final realizando a impressão de cada Nodo do tipo Produto
    # para facilitar a compreencão foi utilizado uma variavel cont para informar a posião dos produtos na lista

    def ImprimeLista(self):
        atual = self.inicio
        cont =0
        print("Inicio da Lista")
        
        if self.inicio == None:
            print("Lista vazia")
        else:
            while atual!=None:
                print(f"Posição: {cont}, {atual}")
                cont = cont+1
                atual = atual.proximo
                
            print("Final da Lista\n")
            
    #Métodos que você deverá desenvolver com o total de produtos possui a necessidade de refrigeração
    
    def TotalProdutoRefrigerado(self):
        
        atual = self.inicio
        cont =0
        
        print("Inicio da Contagem")
        
        if self.inicio == None:
            print("Nenhum Produto refrigerado!")
        else:
            while atual!=None:
                cont = cont + atual.Tipo
                atual = atual.proximo
                
            print(f"Total de Produtos Refrigerados: {cont}")
            print("Fim da contagem!\n")
    
        #return total
        
    # Métodos que adiciona o inicio novo produto
    
    def NovoProduto(self,Nd):
        
        #cria o nodo com o 1 elemento da lista
        atual = self.inicio
        #Atribui ao novo nodo o primiero elemento da lista
        Nd.proximo = atual
        #atualizar o primeiro elemento da lista como sendo o novo elemento
        self.inicio = Nd