# k repetições

import random
v = []
t = int(input("Digite o tamanho do seu vetor:"))
if t <= 0:
    print("Digite um tamanho valido")
else:
    for _ in range(t):
        v.append(random.randint(0,10))
    print(v)
    v.sort()
    print(v)
    maisF = v[0]
    maisRep = 1
    maisAtual = v[0]
    maisRepAtual = 1
    k = int(input("Digite a quantidade de repetições:"))
    for i in range(1,len(v)):
        if v[i] == maisAtual:
            maisRepAtual+=1
        else:
            maisAtual = v[i]
            maisRepAtual = 1
        if maisRepAtual > maisRep:
            maisRep = maisRepAtual
            maisF = v[i]
    if maisRep >= k:
        print(f"Sim, o {maisF} se repete ao menos {k} vezes.")
    else:
        print("Não há")
