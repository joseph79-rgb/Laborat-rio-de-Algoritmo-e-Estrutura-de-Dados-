# Alguém e o dobro
import random

v1 = []
t = int(input("Digite o tamanho: "))
for _ in range(t):
    v1.append(random.randint(0, 99))

if t <= 0:
    print("Insira um tamanho valido.")
else:
    print(v1)
    achei = 0
    for i in range(len(v1)):
        for j in range(i + 1, len(v1)):
            if v1[i] == 2 * v1[j] or v1[j] == 2 * v1[i]:
                print(f"Sim, o par {v1[i]} e {v1[j]}")
                achei = 1
                break 
        
        if achei == 1:
            break
            
    if achei == 0:
        print("Não há")
