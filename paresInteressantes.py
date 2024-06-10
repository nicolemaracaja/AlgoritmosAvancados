#Nicole Brito Maracajá

import math

qtd_testes = int(input())

for caso in range(qtd_testes):
    a, b, c, d = map(int, input().split())
    x, y = -1, -1

    for i in range(a + 1, c + 1):
        if b + (a * b // math.gcd(a * b, i)) - b % (a * b // math.gcd(a * b, i)) <= d:
            y = b + (a * b // math.gcd(a * b, i)) - b % (a * b // math.gcd(a * b, i))
            x = i
            break

    print(x, y)
