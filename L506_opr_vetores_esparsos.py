def busca_por_indice(p, k):
    q = p
    while q:
        if q.indice == k:
            return q.valor
        q = q.proximo
        
    return 0


def busca_por_valor(p, x):
    q = p
    while q:
        if q.valor == x:
            return q.indice
        q = q.proximo
        
    return -1


def atualizacao(p, x, k):
    q = p
    while q:
        if q.indice == k:
            q.valor = x
            break
        q = q.proximo
        
    return p
  #O(E) para cada função, onde E é o número de elementos (não-nulos) armazenados na lista esparsa. Todas as operações percorrem a lista linearmente no máximo uma vez.  
