def lista_lista(p, k):
    L = []
    q = p

    while q:
        inicio = q
        contador = 1

        while q.proximo and contador < k:
            q = q.proximo
            contador += 1

        proximo = q.proximo
        q.proximo = None

        if proximo:
            proximo.anterior = None

        L.append(inicio)
        q = proximo

    return L
  # Complexidade O(N), pois o algoritmo percorre cada elemento da lista original exatamente uma vez para quebrar as conexões e dividi-la nas sublistas, onde N é o número total de elementos. O espaço adicional é O(N/K) para o vetor.
