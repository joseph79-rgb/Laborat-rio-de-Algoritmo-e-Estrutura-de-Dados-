#Impar-Impar
import random

v = []
t = int(input("Digite o tamanho: "))
for _ in range(t):
    v.append(random.randint(0, 99))

if t <= 0:
    print("Insira um tamanho valido.")
else:
    v.sort()
    print(v)
    ja_vistos = []
    
    for i in range(len(v)):
        
        if v[i] % 2 != 0 and v[i] not in ja_vistos:
            contador = 0
            for j in range(len(v)):
                if v[i] == v[j]:
                    contador += 1
                    
            if contador % 2 != 0:
                print(f"O número {v[i]} aparece {contador} vez(es) (ímpar).")
            ja_vistos.append(v[i])
