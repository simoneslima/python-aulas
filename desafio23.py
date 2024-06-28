# num = int(input('Informe um numero:'))
# n = str(num)
# print('Analizando o numero {}'.format(num))
# print('Unidade: {}'.format(n[3]))
# print('Dezena: {}'.format(n[2]))
# print('Centena: {}'.format(n[1]))
# print('Milhar: {}'.format(n[0]))

# Solicita ao usuário que insira um número inteiro
num = int(input('Informe um numero:'))

# Calcula o dígito das unidades (último dígito do número)
u = num // 1 % 10

# Calcula o dígito das dezenas (segundo dígito do número, da direita para a esquerda)
d = num // 10 % 10

# Calcula o dígito das centenas (terceiro dígito do número, da direita para a esquerda)
c = num // 100 % 10

# Calcula o dígito dos milhares (quarto dígito do número, da direita para a esquerda)
m = num // 1000 % 10

# Exibe o número analisado
print('Analisando o numero {}'.format(num))

# Exibe o dígito das unidades
print('Unidade: {}'.format(u))

# Exibe o dígito das dezenas
print('Dezena: {}'.format(d))

# Exibe o dígito das centenas
print('Centena: {}'.format(c))

# Exibe o dígito dos milhares
print('Milhar: {}'.format(m))
