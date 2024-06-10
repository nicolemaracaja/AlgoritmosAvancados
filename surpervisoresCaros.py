#Nicole Brito Maracajá

import math

n = int(input())

qualificacoes = list(map(int, input().split()))
maior_qualificacao = max(qualificacoes)

custo_minimo = [math.inf] * (n + 1) #custo mínimo para cada funcionário

num_aplicacoes = int(input())

for caso in range(num_aplicacoes):
    a, b, c = map(int, input().split())
    custo_minimo[b] = min(custo_minimo[b], c) #atualiza o custo mínimo

indice_raiz = qualificacoes.index(maior_qualificacao) + 1 #posição do funcionário com a maior qualificação
outros_custos = custo_minimo[1:indice_raiz] + custo_minimo[indice_raiz + 1:]

if math.inf in outros_custos:
    print(-1)
else:
    print(sum(outros_custos))
