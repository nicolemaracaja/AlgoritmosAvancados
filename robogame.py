qtd, consulta = [int(x) for x in input().split()]
array = [int(y) for y in input().split()]

i = 0
j = 0 #indice que vai iterar o array

while True:
    if i < consulta:
        i += j
    
    while (i > consulta):
        i -= 1
        j -= 1

    if i == consulta:
        break

    j += 1

print(array[j - 1])
