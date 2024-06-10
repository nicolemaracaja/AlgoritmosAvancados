#Nicole Brito Maracajá

from math import sqrt

r = int(input()) #resultado

k = r - 1 #substituindo pela variavel k na formula
raiz = int(sqrt(k)) #raiz quadrada de k
ok = 0

for i in range(1, raiz + 2): #correcao de quaisquer imprecisao
    if k % i == 0:
        temp = (k / i) - i - 1
        if temp > 0 and temp % 2 == 0:
            ok = 1
            y = temp/2
            print (i, int(y))
            break
if not ok:
    print('NO')
