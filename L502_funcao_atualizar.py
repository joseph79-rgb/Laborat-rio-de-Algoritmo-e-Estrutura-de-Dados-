def Atualizar(self, p, x, y):
    q1 = p
    q2 = None

    while q1 and q1.valor != x:
        q2 = q1
        q1 = q1.proximo

    if q1 is None:
        return p

    if q2 is None:
        p = q1.proximo
        if p:
            p.anterior = None
    else:
        q2.proximo = q1.proximo
        if q1.proximo:
            q1.proximo.anterior = q2

    q1.valor = y
    q1.proximo = None
    q1.anterior = None

    if p is None:
        return q1

    q3 = p
    q4 = None

    while q3 and q3.valor < y:
        q4 = q3
        q3 = q3.proximo

    if q4 is None:
        q1.proximo = p
        p.anterior = q1
        p = q1
    elif q3 is None:
        q4.proximo = q1
        q1.anterior = q4
    else:
        q4.proximo = q1
        q1.anterior = q4
        q1.proximo = q3
        q3.anterior = q1

    return p

# Complexidade O(n)
