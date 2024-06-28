from datetime import date # vai pegar o ano atual
ano = int(input('Que ano quer analizar?'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('È um ano bissexto'.format(ano))
else:
    print('O ano não é bissexto'.format(ano))