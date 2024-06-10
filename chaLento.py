#Nicole Brito Maracajá

qtd_testes = int(input())

for caso in range(qtd_testes):
    qtd_estudantes = int(input())
    tempo_atual = 1
    
    fila = ''
    for e in range(qtd_estudantes):
        intervalo = input().split(' ')
        chegada = intervalo[0]
        saida = intervalo[1]

        while int(chegada) > tempo_atual:
            tempo_atual += 1

        if tempo_atual > int(saida):
            fila += ' 0'
        else:
            fila += f' {tempo_atual}'
            tempo_atual += 1

    print(fila.strip())
