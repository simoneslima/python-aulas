# Solicita a entrada do usuário para a distância em metros
n = float(input('Digite a distância em metros: '))

# Convertendo metros para quilômetros
km = n / 1000  

# Convertendo metros para decâmetros
dam = n / 10

# Convertendo metros para hectômetros
hm = n / 100

# Convertendo metros para centímetros
cm = n * 100

# Convertendo metros para decímetros
dm = n * 10

# Convertendo metros para milímetros
mm = n * 1000

# Imprime a distância em metros e as conversões para outras unidades
print('A distância de {} metros, equivale a {} KM, {} DAM, {} HM, {} CM, {} DM, {} MM.'.format(n, km, dam, hm, cm, dm, mm))





