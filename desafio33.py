n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))
#aqui ja estou dizendo que o menor é o n1
menor = n1
#aqui estou fazendo as comparaçôes
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor numero é {}'.format(menor)) 

#aqui ja estou dizendo que o maior é o n1
maior = n1
#aqui estou fazendo as comparaçôes
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior numero é {}'.format(maior))       