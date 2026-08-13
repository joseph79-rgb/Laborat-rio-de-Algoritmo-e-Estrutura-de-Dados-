class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
      
def tem_repetido(p):
    vistos = []
    atual = p
    while atual is not None:
        for elemento in vistos:
            if elemento == atual.valor:
                return True
        vistos.append(atual.valor)
        atual = atual.proximo
    return False


#O tempo de execução no pior dos casos é O(n²) devido ao laço aninhado.
