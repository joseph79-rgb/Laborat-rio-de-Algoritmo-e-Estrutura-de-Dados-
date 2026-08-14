def vetores_esparsos(V):
    cabeca = None
    cauda = None

    for i in range(len(V)):
        if V[i] != 0:
            novo_no = DNode(V[i], i)
            
            if cabeca is None:
                cabeca = novo_no
                cauda = novo_no
            else:
                cauda.proximo = novo_no
                novo_no.anterior = cauda
                cauda = novo_no

    return cabeca
# Tempo de execução O(n).
