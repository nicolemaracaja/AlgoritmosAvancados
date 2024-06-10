#Nicole Brito Maracajá

qtd_quartos, qtd_vacas = [int(x) for x in input().split(" ")]
quartos = input()
soma = [0] * (qtd_quartos + 1) #vai armazenar a soma de prefixos (1 casa a mais)
saida = meio = indice_inicial = indice_final = 0

def verificar(x): #se eh possivel alocar as vacas no intervalo
    for i in range(qtd_quartos):
        if quartos[i] != '0': #se o quarto estiver ocupado, passa para o prox
            continue

        #indices para a janela deslizante
        a = max(0, i - x) #garante que o inicio da janela n seja menor que 0
        b = min(qtd_quartos - 1, i + x) #garante que o final da janela n ultrapasse o ultimo quarto

        if soma[b + 1] - soma[a] > qtd_vacas:
            return True
    return False

for i in range(qtd_quartos):
    soma[i + 1] = soma[i] + (quartos[i] == '0')
    #se quartos[i] == 0 for true, soma[i] + 1
    #se quartos[i] == 0 for false, soma[i] + 0

indice_inicial, indice_final = 0, qtd_quartos - 1 #busca binaria

while indice_inicial <= indice_final:
    meio = (indice_inicial + indice_final) // 2 #quarto de theo
    if verificar(meio):
        saida = meio
        indice_final = meio - 1
    else:
        indice_inicial = meio + 1

print(saida)
