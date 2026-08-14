def inversao(fila):
    pilha = PilhaEncadeada()

    while not fila.estaVazia():
        pilha.push(fila.dequeue())

    while not pilha.estaVazia():
        fila.enqueue(pilha.pop())

    return fila
# Tempo de execução: O(N), pois cada elemento passa exatamente por um dequeue, um push, um pop e um enqueue, todas sendo operações O(1). O espaço adicional é O(N), já que a pilha armazena todos os elementos simultaneamente. 
