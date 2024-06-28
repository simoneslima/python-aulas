n = str(input('Digite seu Nome Completo: ')).strip()
nome = n.split() 
#vai pegar o primeiro nome do indice [0]
print('Muito prazer em te conhecer! {}'.format(nome[0]))
#ele vai contar o comprimento e mostrar o ultimo nome.
print('Seu Ultimo nome é {}'.format(nome[len(nome)-1]))


