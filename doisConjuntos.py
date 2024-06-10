#Nicole Brito Maracajá

MOD = 10**9 + 7

def count_partition_ways(n):
    total_sum = n * (n + 1) // 2

    if total_sum % 2 != 0:
        return 0
    
    target = total_sum // 2
    
    dp = [0] * (target + 1)
    dp[0] = 1  
    
    for num in range(1, n + 1):
        # Atualizar de forma reversa para evitar reescrever antes do tempo
        for j in range(target, num - 1, -1):
            dp[j] = (dp[j] + dp[j - num]) % MOD
    
    return (dp[target] * 500000004) % MOD  

n = int(input())
print(count_partition_ways(n))
