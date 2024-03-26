total = 0
while True :

    preco  = str(input('Digite o preco'))

    if preco == '=' :
        break
    total += float(preco)
print(total)