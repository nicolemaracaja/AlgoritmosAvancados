#Nicole Brito Maracajá

def pega_indices(seq):
    indice_numero = {}
    for i in range(len(seq)):
        num = seq[i] #obtem o num atual da posicao
        if num not in indice_numero: #se o num n estiver no dicionario, adiciona uma lista vazia p guardar o indice
            indice_numero[num] = []
        indice_numero[num].append(i + 1)  #adiciona o indice associado ao num
    return indice_numero

def processar_consultas(indice_numero, x, k):
    if x not in indice_numero or k > len(indice_numero[x]): #se x n estiver no dicionario ou se k eh maior que o n de oorrencias
        return -1
    else:
        return indice_numero[x][k - 1] 

n, q = [int(x) for x in input().split(' ')]
seq = [int(y) for y in input().split(' ')]

indice_numero = pega_indices(seq)

for saida in range(q):
    x, k = map(int, input().split())
    print(processar_consultas(indice_numero, x, k))
