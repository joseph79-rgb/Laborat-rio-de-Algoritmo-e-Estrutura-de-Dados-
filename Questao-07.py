# Repetidos Próximos

import random
v = []
t = int(input("Digite o tamanho do seu vetor:"))
if t <= 0:
    print("Digite um tamanho valido")
else:
    for _ in range(t):
        v.append(random.randint(0,100))
    print(v)
    k = int(input("Digite a distancia:"))
    achei = 0
    for i in range(len(v)-k):
        if v[i] == v[i+k]:
            print(f"Sim, o {v[i]} nas posições {i} e {i+k}")
            achei = 1
            break
    if achei == 0:
        print("Não há")
