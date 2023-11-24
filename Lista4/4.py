soma_idades = 0
quantidade_individuos = 0

while True:
    idade = int(input())

    if idade < 0:
        break

    soma_idades += idade
    quantidade_individuos += 1

media_idades = soma_idades / quantidade_individuos if quantidade_individuos > 0 else 0

print(f'{media_idades:.2f}')