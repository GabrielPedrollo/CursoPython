n = int(input())
a, b = map(int, input().split())
soma = a + b
if soma <= n:
    print("Farei hoje!")
else:
    print("Deixa para amanha!")