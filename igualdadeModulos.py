#Nicole Brito Maracajá

def igualdadeModulos():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()  #ordenar b
    diferencaMinina = float('inf') #armazena a menor diferenca encontrada
    c = [0] * n  
    for i in range(n):
        diferenca = 0
        if a[i] <= b[0]:
            diferenca = b[0] - a[i]
        else:
            diferenca = m - a[i] + b[0]
        for j in range(n):
            c[j] = (a[j] + diferenca) % m
        c.sort() #ordena c
        if c == b:
            diferencaMinina = min(diferencaMinina, diferenca)

    print(diferencaMinina)

igualdadeModulos()
