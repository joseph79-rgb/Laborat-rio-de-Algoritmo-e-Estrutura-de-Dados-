def Varredura(p):
    q1 = p
    q2 = None

    while q1 and q1.proximo:
        if q1.valor > q1.proximo.valor:
            temp = q1.proximo

            q1.proximo = temp.proximo
            if temp.proximo:
                temp.proximo.anterior = q1

            temp.proximo = q1
            q1.anterior = temp

            if q2 is None:
                temp.anterior = None
                p = temp
            else:
                temp.anterior = q2
                q2.proximo = temp

            q2 = temp
        else:
            q2 = q1
            q1 = q1.proximo

    return p
# Complexidade O(n).
