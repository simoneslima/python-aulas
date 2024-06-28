#uma forma de fazer o calculo
#co = float(input('Comprimento do cateto oposto:'))
#ca = float(input('Comprimento do cateto adiacente:'))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

#outra forma de fazer o calculo é so importar a biblioteca do python
#import math ou tambem
from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adiacente:'))
#hi = math.hypot(co,ca) e retirar o math
hi = hypot(co,ca)
print('A hipoteusa vai medir {:.2f}'.format(hi))



