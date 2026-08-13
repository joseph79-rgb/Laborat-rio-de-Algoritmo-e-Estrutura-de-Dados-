 class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def particionar(p, k):
    menores_inicio = None
    menores_fim = None
    maiores_inicio = None
    maiores_fim = None
    
    atual = p
    while atual is not None:
        proximo = atual.proximo
        atual.proximo = None
        
        if atual.valor <= k:
            if menores_inicio is None:
                menores_inicio = atual
                menores_fim = menores_inicio
            else:
                menores_fim.proximo = atual
                menores_fim = atual
        else:
            if maiores_inicio is None:
                maiores_inicio = atual
                maiores_fim = maiores_inicio
            else:
                maiores_fim.proximo = atual
                maiores_fim = atual
                
        atual = proximo
        
    if menores_inicio is None:
        return maiores_inicio
        
    menores_fim.proximo = maiores_inicio
    return menores_inicio

#Tempo de execução O(n) apenas um laço while
