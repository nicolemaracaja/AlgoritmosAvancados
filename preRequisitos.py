#Nicole Brito Maracajá

from collections import defaultdict, deque

def ordem_cursos(n, m, requisitos):
    grafo = defaultdict(list)
    grau_entrada = [0] * (n + 1)

    for a, b in requisitos:
        grafo[a].append(b)
        grau_entrada[b] += 1

    fila = deque()

    for i in range(1, n + 1):
        if grau_entrada[i] == 0: #cursos sem pre requisitos
            fila.append(i)

    saida = []

    while fila:
        curso = fila.popleft()
        saida.append(curso)

        #removendo o curso processado e atualizando o grau de entrada dos cursos dependentes
        for vizinho in grafo[curso]:
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)

    if len(saida) != n: #verifica se todos os cursos foram processados
        return "IMPOSSIBLE"
    else:
        return saida


n, m = map(int, input().split())
requisitos = []  

for caso in range(m): 
    entrada = input().split()  
    requisito = tuple(map(int, entrada)) 
    requisitos.append(requisito)  

resultado = ordem_cursos(n, m, requisitos)

if resultado == "IMPOSSIBLE":
    print(resultado)
else:
    print(*resultado)
