velocidade = float(input('Qual é a velocidade atual do carro!'))
if velocidade > 80:
    print('Multado! Voce excedeu o limite de 80KM/h. ')
    multa = (velocidade-80) * 7
    print('Voce deve pagar a multa de R${:.2f} !'.format(multa))
print('Tenha uma bom dia e dirija com segurança!..')