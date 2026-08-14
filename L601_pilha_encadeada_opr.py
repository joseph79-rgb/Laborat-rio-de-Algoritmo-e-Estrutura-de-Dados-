def opr_LE():
    pilha = PilhaEncadeada()
    pilha._inserir([42, 17, 5])

    pilha.push(99)
    pilha.push(3)

    removido1 = pilha.pop()
    removido2 = pilha.pop()

    return pilha
  #Tempo de execução: O(1) para cada operação individual de Push e Pop, pois ambas manipulam exclusivamente o ponteiro do topo, sem necessidade de percorrer a estrutura.
