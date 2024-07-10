real = float(input('Quantos reais vc possui para converter-los?'))
dollar = real / 4.97
euro = real / 5.40
print('Com R$ {}{:.2f}{} Reais, você pode comprar USD {}{:.2f}{} em Dollares ou EUR {}{:.2f}{} em Euros.'.format('\033[7;31m',real,'\033[m','\033[7;31m', dollar,'\033[m','\033[7;31m', euro,'\033[m'))
