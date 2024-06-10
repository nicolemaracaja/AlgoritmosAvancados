#Nicole Brito Maracajá

n = int(input())  
seq = list(map(int, input().split())) 

soma_max = float('-inf') 
soma_atual = 0 

for i in range(n):
    soma_atual += seq[i]  
    soma_max = max(soma_max, soma_atual)  
    soma_atual = max(soma_atual, 0)  #reinicia a soma atual para zero se ela se tornar negativa

print(soma_max)  
