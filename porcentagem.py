# Solicita ao usuário o valor do produto
valor = float(input('Digite o valor do produto: '))

# Solicita ao usuário a porcentagem de desconto
porcentagem = int(input('Digite a porcentagem de desconto: '))

# Verifica se a porcentagem está dentro do intervalo válido (0 a 100)
if porcentagem < 0 or porcentagem > 100:
    print("Porcentagem inválida! Por favor, insira uma porcentagem entre 0 e 100.")
else:
    # Calcula o valor total do produto com desconto
    total_com_desconto = valor - (valor * porcentagem / 100)
    print('O total com desconto é R$ {:.2f}'.format(total_com_desconto))
