distancia = float(input('Qual é a distancia da sua viagem?'))
print('Você esta prestes a começar uma viagem de {}Km'.format(distancia))
#ou poderia fazer desse jeito que seria quanse como se fosse ternario uma forma resumida e que funcionara do mesmo jeito.
'''preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45'''

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))