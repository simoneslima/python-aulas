#import random ou
from random import choice
banda1 = str(input('Digite o primeiro nome da banda: '))
banda2 = str(input('Digite o segundo nome da banda: '))
banda3 = str(input('Digite o terceiro nome da banda: '))
banda4 = str(input('Digite o quarto nome da banda: '))
#escolha entre as quatro bandas entre [] lista
lista  = [banda1, banda2, banda3, banda4]
#sorteio = random.choice(lista) ou
sorteio = choice(lista)
print('A banda escolhida foi {}'.format(sorteio))
