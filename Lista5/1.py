v = int(input())

N = [10] * 10

N[0] = v

for i in range(1, 10):
    N[i] = N[i - 1] * 2

for i in range(10):
    print(f'N[{i}] = {N[i]}')