def calcular_diferentes(inicio, fim, alvo, string):  #percorre a string delimitada pelos indices inicio e fim e conta quantos caracteres sao diferentes do alvo
    qtd = 0 #qtd de caracteres diferentes
    for i in range(inicio, fim + 1): #percorre toda a substring
        if string[i] != alvo: #enquanto for diferente do caractere alvo = 'a'
            qtd += 1
    return qtd

def calcular_jogadas(inicio, fim, alvo, string): #funcao recursiva
    if inicio == fim: #se a substring tiver apenas um caractere
        return calcular_diferentes(inicio, fim, alvo, string)

    else:
        minimo_jogadas = float('inf')
        meio = (inicio + fim) // 2

        minimo_jogadas = min(minimo_jogadas, calcular_jogadas(inicio, meio, chr(ord(alvo) + 1), string) + calcular_diferentes(meio + 1, fim, alvo, string))
        minimo_jogadas = min(minimo_jogadas, calcular_jogadas(meio + 1, fim, chr(ord(alvo) + 1), string) + calcular_diferentes(inicio, meio, alvo, string))
        
        return minimo_jogadas

qtd_tentativas = int(input())
for j in range(qtd_tentativas):
    tamanho = int(input())
    entrada = input().strip()
    temp = 'a'
    print(calcular_jogadas(0, tamanho - 1, temp, entrada))
