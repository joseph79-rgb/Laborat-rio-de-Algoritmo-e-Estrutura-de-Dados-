# Elemento Igual na Matriz Quadrada

def matriz_tem_duplicata(M):
    n = len(M)
    for i1 in range(n):
        for j1 in range(n):
            for i2 in range(i1, n):
                if i1 == i2:
                    inicio_j2 = j1 + 1
                else:
                    inicio_j2 = 0
                    
                for j2 in range(inicio_j2, n):
                    if M[i1][j1] == M[i2][j2]:
                        return True
    return False
