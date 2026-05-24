# Numeros Na Interseção

import random
v1 = []
v2 = []
t = int(input("Digite o tamanho:"))
for _ in range(t):
	v1.append(random.randint(0,99))
for _ in range(t):
	v2.append(random.randint(0,99))
if t <= 0:
	print("Insira um tamanho valido.")
else:
	print(v1)
	print(v2)
	ja_visto = []
	for i in range(len(v1)):
		if v1[i] not in ja_visto:
			for j in range(len(v2)):
				if v1[i] == v2[j]:
					print(f"{v1[i]} ésta em ambas os vetores")
					ja_visto.append(v1[i])
					break
		
				
