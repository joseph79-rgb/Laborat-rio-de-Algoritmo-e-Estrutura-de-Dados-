def Particao(p, k):
    if p is None:
        return p

    q = p
    r = p

    while r.proximo:
        r = r.proximo

    while q is not r and q.anterior is not r:

        while q is not r and q.anterior is not r and q.valor <= k:
            q = q.proximo

        while q is not r and q.anterior is not r and r.valor > k:
            r = r.anterior

        if q is r or q.anterior is r:
            break

        q.valor, r.valor = r.valor, q.valor

        q = q.proximo
        r = r.anterior
        
    return p
  #O(N), pois os ponteiros percorrem a lista de forma convergente, visitando cada nó no máximo uma vez.
  
