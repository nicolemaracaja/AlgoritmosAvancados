#Nicole Brito Maracajá

import sys
sys.setrecursionlimit(10**9 + 7)

def exponenciacao_rapida(base, expoente):
    mod = 10**9 + 7
    resultado = 1
    while expoente > 0:
        if expoente % 2 == 1:
            resultado = (resultado * base) % mod
        base = (base * base) % mod
        expoente //= 2
    return resultado

entrada = int(input())

for i in range(entrada):
    a, b = input().split(' ')
    print(exponenciacao_rapida(int(a), int(b)))

