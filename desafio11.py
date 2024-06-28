largura = float(input('Largura da Parede:'))
altura = float(input('Altura da parede : '))
area = largura * altura
print('Com a Largura {} e altura {} temos {} metros quadrados'.format(largura, altura, area))
pintura = area / 2
print('Vai precisar de {} litros de tinta para pintar.'.format(pintura))


