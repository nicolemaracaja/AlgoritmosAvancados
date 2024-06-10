#Nicole Brito Maracajá

tamanho = int(input())
elementos = list(map(int, input().split()))
contagem = 0

for i in range(tamanho):
    if i > 0 and elementos[i - 1]:
        elementos[i - 1] -= 1
    elif elementos[i] == 0 and i < tamanho - 1 and elementos[i + 1]:
        elementos[i + 1] -= 1
    else:
        contagem += 1

print(contagem)
