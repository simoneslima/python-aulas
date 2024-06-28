real = float(input('Quantos reais vc possui para converter-los?'))
dollar = real / 4.97
euro = real / 5.40
print('Com R$ {:.2f} Reais, você pode comprar USD {:.2f} em Dollares ou EUR {:.2f} em Euros.'.format(real, dollar, euro))
