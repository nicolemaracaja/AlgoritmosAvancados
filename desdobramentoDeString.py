#Nicole Brito Maracajá

qtd_testes = int(input())

for n in range(qtd_testes):
    qtd_str = int(input())
    strings = []
    tem_string = {} #ve se a string ja foi lida
    
    for l in range(qtd_str):
        palavra = input()
        strings.append(palavra)
        tem_string[palavra] = True

    for i in range(qtd_str):
        saida = 0
        for j in range(1, len(strings[i])):
            s1 = strings[i][:j] #divide as strings em duas partes
            s2 = strings[i][j:]
            if tem_string.get(s1, False) and tem_string.get(s2, False): #se a chave nao estiver presente no dicionario, assume como false
                saida = 1
                break
        
        print(int(saida), end = '')

    print() #pula uma linha depois da resposta
