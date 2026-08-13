class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
def duplicar_impares(p):
    atual = p
    while atual is not None:
        if atual.valor % 2 != 0:
            novo_no = No(atual.valor)
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
            atual = novo_no.proximo
        else:
            atual = atual.proximo
    return p

# Tempo de execução O(n) devido a percorrer a lista em busca de ímpares.
