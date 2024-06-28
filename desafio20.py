#import randon ou 
from random import shuffle
banda1 = str(input('Digite a primeira banda: '))
banda2 = str(input('Digite a segunda banda: '))
banda3 = str(input('Digite a terceira banda: '))
banda4 = str(input('Digite a quarta banda: '))
#Pro shuffle funcionar é preciso fazer a lista usando colchetes e não parenteses
lista = [banda1, banda2, banda3, banda4]
#o comando shuffle serve para trazer uma lista de modo aleatorio  (sorteado)
#random.shuffle(lista)
shuffle(lista)
print('Voce tocara estas bandas nessa ordem!')
print(lista)
