#Nicole Brito Maracajá

def ultimo_digito(a, b):
    if b == 0:
        return 1 #qualquer num elevado a zero eh um
    
    a = a % 10 #garante que a seja reduzido ao seu ultimo digito

    b = b % 4 #existe um padrao de repeticao do ultimo digito a cada 4 unidades de b

    if b == 0:
        b = 4
    
    return pow(a, b)

qtd_testes = int(input())

for caso in range(qtd_testes):
    a, b = [int(x) for x in input().split()]
    print((str(ultimo_digito(a, b)))[-1])
