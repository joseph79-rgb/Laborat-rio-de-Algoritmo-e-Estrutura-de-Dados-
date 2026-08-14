def Busca(L, x):
    for i in range(len(L)):
        q = L[i]
        
        while q:
            if q.valor == x:
                return q
            if q.valor > x:
                return None
            q = q.proximo
            
    return None


def Insercao(L, x):
    i = 0
    while i < len(L) - 1:
        if L[i + 1] is not None and L[i + 1].valor > x:
            break
        i += 1

    q = L[i]

    if q is None:
        novo = DNode(x)
        L[i] = novo
        return

    novo = DNode(x)

    if x < q.valor:
        novo.proximo = q
        novo.anterior = None
        q.anterior = novo
        L[i] = novo
        return

    while q.proximo and q.proximo.valor < x:
        q = q.proximo

    novo.proximo = q.proximo
    novo.anterior = q

    if q.proximo:
        q.proximo.anterior = novo

    q.proximo = novo


def Remocao(L, x):
    for i in range(len(L)):
        q = L[i]
        
        while q:
            if q.valor == x:
                if q.anterior:
                    q.anterior.proximo = q.proximo
                else:
                    L[i] = q.proximo
                    
                if q.proximo:
                    q.proximo.anterior = q.anterior
                return q
                
            if q.valor > x:
                return None
                
            q = q.proximo
            
    return None
  Tempo de execução: O(M + K) ou O(N/K + K) para todas as três operações, onde M é o número de sublists (N/K) e K é o tamanho de cada sublista, pois há uma varredura linear no vetor e outra na sublista escolhida.  
