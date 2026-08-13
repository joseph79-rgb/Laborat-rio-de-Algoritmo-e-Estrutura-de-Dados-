class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
def separar_pares_impares(inicio):
    list_impares = No(0)
    lista_pares = No(0)
    atual_impar = lista_impares
    atual_par = lista_pares
    atual = inicio
    
    while atual:
        if atual.valor % 2 != 0:
            atual_impar.prox = atual
            atual_impar = atual_impar.prox
        else:
            atual_par.prox = atual
            atual_par = atual_par.prox
            atual = atual.prox
        
    atual_impar.prox = None
    atual_par.prox = None
    
    return lista_impares.prox, lista_pares.prox

  #Tempo de execução: O(n) porquê foi necessário checar a paridade de cada elemento.
