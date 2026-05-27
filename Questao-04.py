# Elemento Isolado

import random
v = []
t = int(input("Digite o tamanho do seu vetor:"))
if t <= 0:
    print("Digite um tamanho valido")
else:
    for _ in range(t):
        v.append(random.randint(0,100))
    print(v)
    elemento_isolado = None
    for i in range(len(v)):
        temVizinho = False
        for j in range(len(v)):
            if i!=j:
                if v[i] == v[j]-1 or v[i] == v[j]+1:
                    temVizinho = True
                    break
        if temVizinho == False:
            elemento_isolado = v[i]
            break
        
    if elemento_isolado != None:
        print(f"Sim, há elemento isolado, o {elemento_isolado}")
    else:
        print("Não há elemento isolado.")
