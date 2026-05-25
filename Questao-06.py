# A Permutação
import random

v1 = []
v2 = []
t = int(input("Digite o tamanho do vetor:"))
if t <= 0:
        print("Digite um tamanho válido.")
else:
    for _ in range(t):
        v1.append(random.randint(0,99))
        v2.append(random.randint(0,99))
        
    print(v1)
    print(v2)
    permutacao = 1
    for i in range(len(v3)):
        encontrado = 0
        for j in range(len(v4)):
            if v3[i] == v4[j]:
                encontrado = 1
                break
        if encontrado == 0:
            permutacao = 0
            break
    if permutacao == 0:
        print("Não são permutações!")
    else:
        print("São permutações!")
                         
                      
