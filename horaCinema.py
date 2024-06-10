#Nicole Brito Maracajá

n = int(input())
filmes = []

for caso in range(n):
    a, b = map(int, input().split())
    filmes.append((a, b))

filmes.sort(key=lambda x: x[1]) #ordena os filmes pelo horario de termino

assistidos = 0
ultimo_termino = 0

for inicio, fim in filmes:
    if inicio >= ultimo_termino:
        assistidos += 1
        ultimo_termino = fim

print(assistidos)
