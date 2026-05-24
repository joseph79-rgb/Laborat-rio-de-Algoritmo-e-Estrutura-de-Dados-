import random
v = []
k = int(input("Digite o tamanho:"))
for _ in range(k):
	v.append(random.randint(0,99))
if k <= 0:
	print("Digite um tamanho valido")
else:
	print(v)
	contador = 0
	for i in range(len(v)):
		for j in range(i+1, len(v)):
			if v[i] > v[j]:
				contador+=1
	print(f"O vetor possui {contador} inversoes")
