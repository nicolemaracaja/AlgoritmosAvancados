#Nicole Brito Maracajá

import heapq
from collections import defaultdict

n, m = list(map(int, input().split()))
grafo = defaultdict(list)

for caso in range(m):
    src, des = list(map(int, input().split()))
    grafo[src].append(des)
    grafo[des].append(src)

origem = 1
heap = []
resultado = []
visitados = set()

def bfs(origem):
    heapq.heappush(heap, origem)
    while heap:
        no_atual = heapq.heappop(heap)
        if no_atual in visitados:
            continue
        
        resultado.append(no_atual)
        visitados.add(no_atual)

        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                heapq.heappush(heap, vizinho)

    return resultado

print(*bfs(origem))
