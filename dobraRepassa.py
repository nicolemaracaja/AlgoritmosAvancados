#Nicole Brito Maracajá

from collections import deque

a, b = map(int, input().split(' '))

visitados = {}
fila = deque([a])

while fila:
    v = fila.popleft()
    
    if 2 * v not in visitados and 2 * v <= b:
        fila.append(2*v)
        visitados[2*v] = v
    
    if 10 * v + 1 not in visitados and 10 * v + 1 <= b:
        fila.append(10*v+1)
        visitados[10*v+1] = v

if b not in visitados:
    print("NO")  
else:
    sequencia = [b]
    while sequencia[-1] != a:
        sequencia.append(visitados[sequencia[-1]])

    print("YES") 
    print(len(sequencia))  
    print(*reversed(sequencia))  
