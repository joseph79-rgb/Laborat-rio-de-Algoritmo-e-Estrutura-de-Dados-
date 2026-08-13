 class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def inverter_lista(p):
    anterior = None
    atual = p
    while atual is not None:
        proximo = atual.proximo
        atual.proximo = anterior
        anterior = atual
        atual = proximo
    return anterior

#Tempo de execução O(n), a lista é percorrida apenas uma vez enquanto inverte as referências dos ponteiros.
