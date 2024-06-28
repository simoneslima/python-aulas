from random import randint
from time import sleep  #faz o pc esperar como se estivesse pensando
computador = randint(0,5) #aqui o pc vai sortear o numero
print ('-=-'* 20) #para fazer uma linha como separador 
print ('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print ('-=-'* 20) #para fazer uma linha como separador 
jogador = int(input('Em que numero eu pensei? ')) #o jogador tenta advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabens! Voce conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no numero {}'.format(computador, jogador))
