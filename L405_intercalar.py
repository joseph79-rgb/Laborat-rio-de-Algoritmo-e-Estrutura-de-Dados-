 class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def intercalar(p1, p2):
    if p1 is None: 
        return p2
    if p2 is None: 
        return p1
    
    if p1.valor < p2.valor:
        inicio = p1
        p1 = p1.proximo
    else:
        inicio = p2
        p2 = p2.proximo
        
    atual = inicio
    
    while p1 is not None and p2 is not None:
        if p1.valor < p2.valor:
            atual.proximo = p1
            p1 = p1.proximo
        else:
            atual.proximo = p2
            p2 = p2.proximo
        atual = atual.proximo
        
    if p1 is not None:
        atual.proximo = p1
    if p2 is not None:
        atual.proximo = p2
        
    return inicio

#Tempo de execução O(n) pelo laco while percorrer a lista.
