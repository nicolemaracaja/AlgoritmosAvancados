#Nicole Brito Maracajá

n, a, b, c = map(int, input().split())

# Inicialização do vetor dp para representar o número máximo de pedaços possíveis
dp = [-1] * (n + 1)
dp[0] = 0  #para comprimento zero, não há cortes

for i in range(1, n + 1):
    # Para cada comprimento permitido (a, b, c), atualize o vetor dp
    if i >= a and dp[i - a] != -1:
        dp[i] = max(dp[i], dp[i - a] + 1)
    if i >= b and dp[i - b] != -1:
        dp[i] = max(dp[i], dp[i - b] + 1)
    if i >= c and dp[i - c] != -1:
        dp[i] = max(dp[i], dp[i - c] + 1)

print(dp[n])
