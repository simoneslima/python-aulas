salario = float(input('Qual é o salario sem o aumento?'))
porcentagem = int(input('Qual a porcentagem que vai colocar em cima?'))
aumento = salario + (salario * porcentagem / 100)
print('O salario com o aumento de {}% vai ser de R${:.2f}.'.format(porcentagem, aumento))
