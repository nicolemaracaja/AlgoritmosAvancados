#Nicole Brito Maracajá

def findLCS(str1, str2):
    m = len(str1)
    n = len(str2)

    #Criar uma tabela para armazenar comprimentos da LCS
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Preencher a tabela com comprimentos da LCS
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                #se os caracteres são iguais, a lcs cresce
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                #se não são iguais, pega o maior valor das opções anteriores
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Agora, precisamos reconstruir a LCS a partir da tabela
    lcs = []
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            # Se os caracteres são iguais, eles fazem parte da LCS
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Como reconstruímos a LCS de trás para frente, precisamos inverter antes de retornar
    lcs.reverse()

    return "".join(lcs)

str1 = input()
str2 = input()

print(findLCS(str1, str2))
