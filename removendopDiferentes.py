#Nicole Brito Maracajá

qtd_testes = int(input())
resp = [0] * qtd_testes

for i in range(qtd_testes):
  comprimento_array = int(input()) 
  array = [int(num) for num in input().split()]
  array.sort()
  maior = -1

  for num in array:
        if maior == -1:
            numero = num
            maior = 1
            cont = 1
        elif num == numero:
            cont += 1
            if cont > maior:
              maior = cont
        else:
            numero = num
            cont = 1

  if comprimento_array % 2 == 0:
    sobra = maior - comprimento_array//2
    if sobra > 0:
      resp[i] = sobra * 2

  else:
    sobra = maior - (comprimento_array//2 + 1)
    if sobra < 0:
       sobra = 0
    resp[i] = 1 + (2*sobra)

for e in resp:
  print(e)
