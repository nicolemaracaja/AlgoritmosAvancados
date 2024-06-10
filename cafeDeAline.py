#Nicole Brito Maracajá

n, k, q = [int(x) for x in input().split()]
# n = qtd de receitas que aline conhece
# k = qtd de receitas admissiveis
# q = qtd de perguntas que aline faz

receitas = [0] * (200000 + 2) #conta qts receitas recomendam cada temp

for i in range(n):
    a, b = [int(y) for y in input().split()]
    receitas[a] += 1 #incrementa na lista de zeros, mostrando aonde comecam as indicacoes (1)
    receitas[b + 1] -= 1 #indica onde termina de incrementar (-1)

for j in range(1, len(receitas)): #soma de prefixos para saber quais as receitas recomendadas
    receitas[j] += receitas[j - 1]

for l in range(1, len(receitas)): #soma de prefixos para saber quais as receitas aparecem k vezes
    if receitas[l] >= k:
        receitas[l] = 1 #se aparecer mais de k vezes, mostra 1
    else:
        receitas[l] = 0 #se n, mostra 0
    receitas[l] += receitas[l - 1]

for m in range(q): #perguntas de aline
    c, d = [int(w) for w in input().split()]
    print(receitas[d] - receitas[c - 1]) #qtd de admissiveis dentro do intervalo

