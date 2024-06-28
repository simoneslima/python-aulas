nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
media = (nota1 + nota2)/ 2
print('Sua media foi {:.1f}'.format(media))
if media >= 6.0:
    print('Sua media foi Boa! Parabens!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!') 

#dá para simplificar ainda mais como:
#print ('Parabens' if media >=6.0 else 'estude mais')   
