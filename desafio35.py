print('-=' * 20)
print('Analizador de Triangulos')
print('-=' * 20)
angulo1 = float(input('Primeiro Angulo: '))
angulo2 = float(input('Segundo Angulo: '))
angulo3 = float(input('Terceiro Angulo: '))
if angulo1 < angulo2 + angulo3 and angulo2 < angulo1 + angulo3 and angulo3 < angulo1 + angulo2:
    print('Os Angulos acima podem formar um triângulo! ')
else:
    print('Os Angulos acima não podem formar um triâgulo! ')