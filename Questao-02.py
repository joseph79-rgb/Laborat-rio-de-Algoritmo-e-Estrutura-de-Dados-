# O k_esimo maior
import random
v = []
t = int(input("Digite o tamanho do seu vetor:"))
if t <= 0:
    print("Digite um tamanho valido")
else:
    for _ in range(t):
        v.append(random.randint(0,100))
    print(v)
    v.sort()
    print(v)
    k = int(input("Insira qual maior você quer:"))
    if k <= 0 or k > t:
        print("posição invalida para esse vetor.")
    else:
        indice_procurado = len(v)-k
        k_esimoMaior = v[indice_procurado] 
        print(f"O {k}_esimo maior é {k_esimoMaior}.")
