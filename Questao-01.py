# O terceiro maior elemento
import random
v = []
k = int(input("Digite o tamanho do seu vetor:"))
if k <= 0:
    print("Digite um tamanho valido")
else:
    for _ in range(k):
        v.append(random.randint(0,100))
    print(v)
    Maior = None
    segMaior = None
    tercMaior = None
    
    for i in range(len(v)):
        if Maior == None or v[i] > Maior:
            tercMaior = segMaior
            segMaior = Maior
            Maior = v[i]
        elif (segMaior == None or v[i] > segMaior) and v[i] != Maior:
            tercMaior = segMaior
            segMaior = v[i]
        elif (tercMaior == None or v[i] > tercMaior) and v[i] != Maior and v[i] != segMaior:
            tercMaior = v[i]
    if Maior == None:
        print("Não há numeros")
    elif segMaior == None:
        print(f"Só há um numero: {Maior}")
    elif tercMaior == None:
        print("Só há dois numeros:")
        print(f"Maior: {Maior}")
        print(f"Segundo Maior: {segMaior}")
    else:
        print(f"Maior: {Maior}")
        print(f"Segundo Maior: {segMaior}")
        print(f"Terceiro Maior: {tercMaior}")
