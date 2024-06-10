#Nicole Brito Maracajá

qtd_testes = int(input())

for caso in range(qtd_testes):
    qtd_letras = int(input())
    divisor = 1
    while qtd_letras % divisor == 0:
        divisor += 1
    for i in range(qtd_letras):
        print(chr(i % divisor + 97), end='')
    print()
