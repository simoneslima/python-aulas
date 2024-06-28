# ou poderia ter usado o floor no lugar do trunc que vai mostrar o valor #cortando os numeros flutuantes para inteiro
from math import factorial, trunc, sqrt
numero = int(input('Digite um numero:'))
fatorial = factorial(numero)
raiz = sqrt(numero)
print('O fatorial de {} é {} e a raiz quadrada de {} é {}'.format(numero, trunc(fatorial), numero, trunc(raiz)))



