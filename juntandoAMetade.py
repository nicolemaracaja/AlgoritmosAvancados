#Nicole Brito Maracajá

import math

t = int(input())

for caso in range(t):
    n, W = map(int, input().split())
    weights = list(map(int, input().split()))  #peso dos itens

    #calcula os pesos min e max
    peso_minimo = math.ceil(W / 2) #peso min que queremos atingir
    peso_maximo = W  #peso que n pode ultrapassar
    
    itens_validos = []
    peso_total = 0  
    
    item_perfeito = False
    for i, peso in enumerate(weights):
        if peso_minimo <= peso <= peso_maximo: #encontra um item no intervalo desejado
            itens_validos = [i + 1] 
            item_perfeito = True
            break  #pode parar de procurar
    
    if item_perfeito:
        print(1) 
        print(itens_validos[0])  #indice do item
        continue  
    
    #combina itens menores para atingir o peso
    for i, peso in enumerate(weights):
        if peso_total + peso <= peso_maximo:
            itens_validos.append(i + 1)  
            peso_total += peso #atualiza o peso
            if peso_total >= peso_minimo:  #se o peso total atingir ou ultrapassar o peso min, para
                break
    
    if peso_total >= peso_minimo:
        print(len(itens_validos)) 
        print(" ".join(map(str, itens_validos))) 
    else:
        print(-1)  
