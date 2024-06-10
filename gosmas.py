#Nicole Brito Maracajá

def calcular_soma_subarray(inicio, fim, prefixos):
    # Retorna a soma do subarray entre os índices inicio e fim usando a soma prefixa
    if inicio == 0:
        return prefixos[fim]
    return prefixos[fim] - prefixos[inicio - 1]

def encontrar_custo_minimo(inicio, fim, prefixos, tabela_dp):
    if inicio == fim:
        return 0
    if inicio > fim:
        return 0

    if tabela_dp[inicio][fim] != -1:
        return tabela_dp[inicio][fim]

    custo_minimo = float('inf')

    for divisao in range(inicio, fim):
        custo_esquerda = encontrar_custo_minimo(inicio, divisao, prefixos, tabela_dp)
        custo_direita = encontrar_custo_minimo(divisao + 1, fim, prefixos, tabela_dp)
        custo_combinacao = calcular_soma_subarray(inicio, fim, prefixos)
        custo_total = custo_esquerda + custo_direita + custo_combinacao
        custo_minimo = min(custo_minimo, custo_total)

    tabela_dp[inicio][fim] = custo_minimo
    return tabela_dp[inicio][fim]


n = int(input())
elementos = list(map(int, input().split()))

prefixos = [0] * n
prefixos[0] = elementos[0]

for i in range(1, n):
    prefixos[i] = prefixos[i - 1] + elementos[i]

tabela_dp = [[-1 for _ in range(n)] for _ in range(n)]
custo_minimo = encontrar_custo_minimo(0, n - 1, prefixos, tabela_dp)
print(custo_minimo)
