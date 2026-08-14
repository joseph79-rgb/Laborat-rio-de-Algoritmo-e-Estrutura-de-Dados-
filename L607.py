class Solucao:
    def contraExemploPilha(self):
        print("(a) Entrada: 42, 12 (nessa ordem). Dígito das unidades igual (2) para ambos.")
        print("(a) Com filas (estável):   saem na ordem 42, 12 -> ordem relativa preservada.")
        print("(a) Com pilhas (instável): sairiam na ordem 12, 42 -> ordem relativa invertida.")

    def radixSort(self, numeros, numDigitos):
        sequencia = list(numeros)

        for passagem in range(numDigitos):
            filas = [FilaEncadeada() for _ in range(10)]

            for numero in sequencia:
                digito = (numero // (10 ** passagem)) % 10
                filas[digito].enqueue(numero)

            print(f"\nPassagem {passagem + 1} (dígito na posição {passagem}, peso 10^{passagem}):")

            for d in range(10):
                if not filas[d].estaVazia():
                    print(f"  Fila {d}:", end=" ")
                    filas[d].exibir()

            sequencia = []

            for d in range(10):
                while not filas[d].estaVazia():
                    sequencia.append(filas[d].dequeue())

            print(f"  Sequência coletada após a passagem {passagem + 1}: {sequencia}")

        return sequencia
