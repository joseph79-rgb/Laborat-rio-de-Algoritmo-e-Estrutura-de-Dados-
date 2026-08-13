 class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
de
f maior_no_fim(p):
    if p is None or p.proximo is None:
        return p
    
    atual = p
    maior = p
    anterior_maior = None
    anterior = None
    
    while atual is not None:
        if atual.valor > maior.valor:
            maior = atual
            anterior_maior = anterior
        anterior = atual
        atual = atual.proximo
        
    if maior.proximo is None:
        return p
        
    if anterior_maior is None:
        p = p.proximo
    else:
        anterior_maior.proximo = maior.proximo
        
    ultimo = p
    while ultimo.proximo is not None:
        ultimo = ultimo.proximo
        
    ultimo.proximo = maior
    maior.proximo = None
    
    return p

#O tempo de execução é O(n) pois percorreu a lista inteira em busca do maior elemento e o último nó.
