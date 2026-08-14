def Função Enqueue(valor):
    P1.Push(valor)
def Função Dequeue():
    Se P2 estiver vazia:
        Enquanto P1 não estiver vazia:
            P2.Push(P1.Pop())
    Retornar P2.Pop()
from PE import PilhaEncadeada

class FilaComDuasPilhas:
    def __init__(self):
        self.p1 = PilhaEncadeada()  # Pilha de entrada
        self.p2 = PilhaEncadeada()  # Pilha de saída

    def enqueue(self, valor):
        """A inserção sempre empilha em P1, com custo O(1)."""
        self.p1.push(valor)

    def dequeue(self):
        """
        Retira o topo de P2. Se P2 estiver vazia, transfere todos 
        os elementos de P1 para P2 invertendo a ordem (LIFO para FIFO).
        """
        if self.p2.estaVazia():
            while not self.p1.estaVazia():
                self.p2.push(self.p1.pop())

        return self.p2.pop()

    def exibir(self):
        print("P1 (entrada):", end=" ")
        self.p1.exibir()
        print("P2 (saída):", end=" ")
        self.p2.exibir()


class Solucao:
    def executar(self):
        fila = FilaComDuasPilhas()

        fila.enqueue(1)
        fila.enqueue(2)
        fila.enqueue(3)

        print("Após Enqueue(1), Enqueue(2), Enqueue(3):")
        fila.exibir()

        removido = fila.dequeue()
        print(f"\nDequeue() removeu {removido} (P2 estava vazia, houve transferência P1 -> P2):")
        fila.exibir()

        fila.enqueue(4)
        removido = fila.dequeue()
        print(f"\nEnqueue(4) e depois Dequeue() removeu {removido} (P2 não estava vazia, sem transferência):")
        fila.exibir()

if __name__ == "__main__":
    s = Solucao()
    s.executar()
  
