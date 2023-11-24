valor_a, valor_b =map(int, input().split())
if(valor_a%valor_b==0) or (valor_b%valor_a==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")