# O mais próximo da média

import random
v = []
k = int(input("Digite o tamanho do seu vetor:"))
if k <= 0:
    print("Digite um tamanho valido")
else:
    for _ in range(k):
        v.append(random.randint(0,100))
    print(v)
    
    soma = 0
    for i in range(len(v)):
        soma = soma + v[i]
    media = soma // (len(v))
    MenorDiff = abs(v[0]-media)
    maisProximo = v[0]
    for i in range(len(v)):
        diffAtual = abs(v[i]-media)
        if diffAtual < MenorDiff:
            MenorDiff = diffAtual
            maisProximo = v[i]
    
    print(f"O mais proximo é {maisProximo}")
