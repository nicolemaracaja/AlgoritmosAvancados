#Nicole Brito Maracajá

S, N = map(int, input().split())

dp = [0] * (S + 1) #armazena o valor máximo

for caso in range(N):
    tamanho, valor = map(int, input().split())
    
    #atualizar o vetor dp para incluir o item
    for capacidade in range(S, tamanho - 1, -1):
        dp[capacidade] = max(dp[capacidade], dp[capacidade - tamanho] + valor)

print(dp[S])
