#Nicole Brito Maracajá

entrada = input()
saida = list(entrada) #inicia com uma lista dos caracteres da entrada
tamanho = len(entrada)

for i in range(tamanho - 2, -1, -1):
    saida[i] = min(saida[i], saida[i + 1])

saida.append('z')
pilha = []
resultado = ""

for i in range(tamanho):
    pilha.append(entrada[i])
    while pilha and pilha[-1] <= saida[i + 1]:
        resultado += pilha.pop()

print(resultado)
