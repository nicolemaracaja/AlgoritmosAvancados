#Nicole Brito Maracajá

import math
 
a, b = [int(x) for x in input().split()]
 
if a == b: #todos os nums sao divisiveis por si mesmo
    print("infinity")
elif a < b: #n ha nums maiores que b que sejam divisiveis por a-b
    print(0)
else:
    c = a - b 
    raiz = int(math.sqrt(c)) #limite superior
    cont = 0
    for i in range(1, raiz + 1):
        if c % i == 0:
            q = c // i #quociente 
            if i > b: #i eh divisor de c e maior que b
                cont += 1
            if i != q and q > b:
                cont += 1
    print(cont)
