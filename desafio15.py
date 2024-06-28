dias = int(input('Digite os dias alugados: '))
km = float(input('Quantos km rodados: '))
valor = (dias * 60) + (km * 0.15)
print('O total a pagar é {:.2f} reais'.format(valor))