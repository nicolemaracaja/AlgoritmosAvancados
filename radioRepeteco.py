#Nicole Brito Maracajá

n = int(input())
playlist = [int (x) for x in input().split()]

inicio = 0
comprimento_maximo = 0
conjunto_musicas = set()  #evita repeticoes

for i in range(n):
    if playlist[i] not in conjunto_musicas:
        conjunto_musicas.add(playlist[i])
        comprimento_maximo = max(comprimento_maximo, i - inicio + 1)
    else:
        while playlist[inicio] != playlist[i]:
            conjunto_musicas.remove(playlist[inicio])
            inicio += 1
        inicio += 1

print(comprimento_maximo) 
