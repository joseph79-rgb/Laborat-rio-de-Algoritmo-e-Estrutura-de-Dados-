def balanceamento_delimitador(expressao):
    pares = {')': '(', ']': '[', '}': '{'}
    abridores = set(pares.values())

    pilha = PilhaEncadeada()

    for i, caractere in enumerate(expressao):
        if caractere in abridores:
            pilha.push(caractere)
        elif caractere in pares:
            if pilha.estaVazia():
                return (False, i, caractere, "fechador sem abridor correspondente")

            topo = pilha.pop()

            if topo != pares[caractere]:
                return (False, i, caractere, f"esperava fechar '{topo}', mas encontrou '{caractere}'")

    if not pilha.estaVazia():
        return (False, len(expressao), pilha.pop(), "abridor sem fechador correspondente")

    return (True, None, None, None)
#Tempo de Execução: O(n).
