#Nicole Brito Maracajá

testes = int(input())

for caso in range(testes):
    tamanho = int(input())
    permutacao = list(map(int, input().split()))
    posicao = [0] * tamanho

    for i in range(tamanho):
        elemento = permutacao[i]
        posicao[elemento-1] = i
        
    operacoes = tamanho // 2

    while operacoes and posicao[operacoes - 1] < posicao[operacoes] and posicao[tamanho - operacoes] > posicao[tamanho - operacoes - 1]:
        operacoes -= 1
    print(operacoes)
