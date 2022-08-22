import conversor as c   # importa o arquivo de conversao

print("\n---------- Conversor de número para extenso ----------")
while True:
    num = input("Digite um numero de 1 a 999 -> ") # recebe o numero do usuario
    if num == '' or not num.isnumeric() or int(num) > 999 or int(num) < 1:  # verifica se o numero é válido
        print('Esse valor não é aceito, tente colocar um número de 1 a 1000!')
    else:
        print("\n" + c.converte(str(num)) + "\n")