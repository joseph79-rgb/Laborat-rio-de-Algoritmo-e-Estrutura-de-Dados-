class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
      
def intersecao(p1, p2):
    p_inicio = None
    p_atual = None
    atual1 = p1
    while atual1 is not None:
        atual2 = p2
        encontrou = False
        while atual2 is not None:
            if atual1.valor == atual2.valor:
                encontrou = True
                break
            atual2 = atual2.proximo
        if encontrou:
            verifica = p_inicio
            ja_existe = False
            while verifica is not None:
                if verifica.valor == atual1.valor:
                    ja_existe = True
                    break
                verifica = verifica.proximo
            if not ja_existe:
                novo_no = No(atual1.valor)
                if p_inicio is None:
                    p_inicio = novo_no
                    p_atual = novo_no
                else:
                    p_atual.proximo = novo_no
                    p_atual = novo_no
        atual1 = atual1.proximo
    return p_inicio
  
#O tempo de execução é O(N x M), onde N e M são os comprimentos das listas iniciais.
