 class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
      
def elemento_mais_frequente(p):
    contagens = {}
    atual = p
    
    while atual is not None:
        if atual.valor in contagens:
            contagens[atual.valor] = contagens[atual.valor] + 1
        else:
            contagens[atual.valor] = 1
        atual = atual.proximo
        
    mais_frequente = None
    maior_contagem = 0
    
    for valor in contagens:
        if contagens[valor] > maior_contagem:
            maior_contagem = contagens[valor]
            mais_frequente = valor
            
    return mais_frequente, maior_contagem
  #Tempo de execução O(n)
