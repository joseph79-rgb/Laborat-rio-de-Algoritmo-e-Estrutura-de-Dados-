 class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
 
def remover_copias(p, k):
    while p is not None and p.valor == k:
        p = p.proximo
        
    if p is None:
        return None
        
    atual = p
    while atual.proximo is not None:
        if atual.proximo.valor == k:
            atual.proximo = atual.proximo.proximo
        else:
            atual = atual.proximo
            
    return p
  #Tempo de execução O(n) apenas um laço while.
