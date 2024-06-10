#Nicole Brito Maracajá

qtd_testes = int(input())

for caso in range(qtd_testes):
    a, b, c = map(int, input().split())
    x = 10**(a-1)
    y = 10**(b-1)
    z = 10**(c-1)
    print(x, y + z)
