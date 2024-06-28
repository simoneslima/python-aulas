#modo de fazer
# import math
# ângulo = float(input('Digite um angulo:'))
# seno = math.sin(math.radians(ângulo))
# print('O angulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
# cosseno = math.cos(math.radians(ângulo))
# print('O angulo de {} tem o cosseno de {:.2f} '.format(ângulo, cosseno))
# tangente = math.tan(math.radians(ângulo))
# print('O angulo de {} em tangente é {:.2f}'.format(ângulo, tangente))
# outro modo que funciona do mesmo jeito
from math import radians, sin, cos, tan 
ângulo = float(input('Digite um angulo:'))
seno = sin(radians(ângulo))
print('O angulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O angulo de {} tem o cosseno de {:.2f} '.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O angulo de {} em tangente é {:.2f}'.format(ângulo, tangente))
