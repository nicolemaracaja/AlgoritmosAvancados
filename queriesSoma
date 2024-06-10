entrada = [int(x) for x in input().split(" ")] 
array = [int(y) for y in input().split(" ")]

listaSomas = []
numSoma = 0

for num in array: 
    numSoma += num
    listaSomas.append(numSoma)

for i in range(entrada[1]):
    intervalos = [int(n) for n in input().split(" ")]
    a, b = intervalos
    print(listaSomas[b - 1] + array[a - 1] - listaSomas[a - 1])
