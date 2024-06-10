#Nicole Brito Maracajá

def max_soma(n, array):
    ponteiro_esquerdo = 0
    ponteiro_direito = n - 1 #começa do final do array
    soma1 = 0
    soma3 = 0
    max_soma = 0

    while ponteiro_esquerdo <= ponteiro_direito: #tecnica dos dois ponteiros (extremos)
        if soma1 == soma3:
            max_soma = soma1

        if soma1 <= soma3:
            soma1 += array[ponteiro_esquerdo] #soma do inicio
            ponteiro_esquerdo += 1
        else:
            soma3 += array[ponteiro_direito] #soma do final
            ponteiro_direito -= 1 

    if soma1 == soma3:
        max_soma = soma1

    return max_soma

qtd = int(input())
sequencia = [int(x) for x in input().split()]

print(max_soma(qtd, sequencia))
