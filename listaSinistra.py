#Nicole Brito Maracajá

casosTestes = int(input())

for caso in range(casosTestes):

    comprimento, valor = [int(y) for y in input().split(' ')]
    array = [int(x) for x in input().split(' ')]
    array_aux = [1 for item in array] #inicia com 1 em casa posicao

    i = 0
    while (array[i] % valor == 0):
        if array[i] / valor == array[len(array) - 1]:
            array_aux[len(array) - 1] += valor
        else:
            array.append(array[i]//valor)
            array_aux.append(valor * array_aux[i])
        i += 1

    soma = 0
    for j in range(len(array)):
        soma += array[j] * array_aux[j]

    print(soma)
