class DNode:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


def imprime_elemento_central(p):
    if p is None:
        return None

    q1 = p
    q2 = p

    while q1.proximo and q1.proximo.proximo:
        q1 = q1.proximo.proximo
        q2 = q2.proximo

    print(q2.valor)
    return q2
# Complexidade O(n).
