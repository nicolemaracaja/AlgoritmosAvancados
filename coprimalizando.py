#Nicole Brito Maracajá

import math

tamanho = int(input())
array = list(map(int, input().split()))
saida = []
cont = 0

for i in range(tamanho):
    if i > 0 and math.gcd(array[i-1], array[i]) != 1:
        saida.append(1)
        cont += 1
    saida.append(array[i])

print(cont)

resposta = ''
for elem in saida:
    resposta += f' {elem}'

print(resposta.strip())
