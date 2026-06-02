# Linhas Iguais na Matriz Quadrada

def linhas_iguais_matriz(M):
    n = len(M)
    for i in range(n):
        for j in range(i + 1, n):
            if M[i] == M[j]:  
                return f"Sim, as linhas {i} e {j} são iguais."
    return "Não foram encontradas linhas iguais."
  
