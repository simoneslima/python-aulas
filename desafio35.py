print('-=' * 20)
#Coloquei uma cor 
print('\033[4;30;45mAnalizador de Triangulos\033[m')
print('-=' * 20)
angulo1 = float(input('Primeiro Angulo: '))
angulo2 = float(input('Segundo Angulo: '))
angulo3 = float(input('Terceiro Angulo: '))
if angulo1 < angulo2 + angulo3 and angulo2 < angulo1 + angulo3 and angulo3 < angulo1 + angulo2:
    print('\033[7;33;40mOs Angulos acima podem formar um triângulo!\033[m ')
else:
    print('\033[7;37;41mOs Angulos acima não podem formar um triâgulo!\033[m')