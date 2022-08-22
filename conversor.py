centenas = {'1': 'Cem', '11': 'Cento', '2': 'Duzentos', '3': 'Trezentos', '4': 'Quatrocentos', '5': 'Quinhentos', '6': 'Seiscentos', '7': 'Setecentos', '8': 'Oitocentos', '9': 'Novecentos'}
dezenas = {'1': 'dez', '2': 'vinte', '3': 'trinta', '4': 'quarenta', '5': 'cinquenta', '6': 'sessenta', '7': 'setenta', '8': 'oitenta', '9': 'noventa'}
dez_ate_20 = {'11': 'onze', '12': 'doze', '13': 'treze', '14': 'quatorze', '15': 'quinze', '16': 'dezesseis', '17': 'dezessete', '18': 'dezoito', '19': 'dezenove'}
unidade = {'1': 'um', '2': 'dois', '3': 'três', '4': 'quatro', '5': 'cinco', '6': 'seis', '7': 'sete', '8': 'oito', '9': 'nove'}

def converte_unidade(strnum):
    return unidade[f'{strnum}'] if len(strnum) == 1 else '0'


def converte_dezena(frst_index_num, last_index_num, strnum):
    dezena_ = int(frst_index_num + last_index_num)

    if frst_index_num + '0' == strnum: # caso seja 30 por exemplo
        return dezenas[f'{frst_index_num}']

    # VERIFICACOES ESPECIFICAS DA DEZENA 1
    if dezena_ > 10 and dezena_ < 20:
        return dez_ate_20[f'{dezena_}']

    # VERIFICACOES DOS OUTROS NUMEROS
    if frst_index_num + last_index_num == strnum:
        return dezenas[f'{frst_index_num}'] + ' e ' + unidade[f'{last_index_num}']

        
def converte_centena(frst_index_num, middle_index_num, last_index_num, strnum):  # funcao que converte centenas
    dezena_ = int(middle_index_num + last_index_num)

    if frst_index_num + '00' == strnum: # veririca se o numero corresponde ao inserido, ex: se 100 é igual a 100
        return centenas[f'{frst_index_num}']


    # VERIFICACOES ESPECIFICAS DA CENTENA 1
    if '10' + last_index_num == strnum: # caso seja 101 por exemplo
        return centenas['11'] + ' e ' + unidade[f'{last_index_num}']

    elif '1' + middle_index_num + '0' == strnum: # caso seja 110 por exemplo
        return centenas['11'] + ' e ' + dezenas[f'{middle_index_num}']
    
    elif dezena_ > 10 and dezena_ < 20: # caso seja 115 por exemplo
        if '1' + middle_index_num + last_index_num == strnum:
            return centenas['11'] + ' e ' + dez_ate_20[f'{middle_index_num + last_index_num}']
    
    elif '1' + middle_index_num + last_index_num == strnum: # caso a dezena seja maior que 19, 120 por exemplo
        return centenas['11'] + ' e ' + dezenas[f'{middle_index_num}'] + ' e ' + unidade[f'{last_index_num}']


    # VERIFICACOES DOS OUTROS TIPOS DE NUMEROS
    if frst_index_num + '0' + last_index_num == strnum: #caso seja 303 por exemplo
        return centenas[f'{frst_index_num}'] + ' e ' + unidade[f'{last_index_num}']

    elif frst_index_num + middle_index_num + '0' == strnum: # caso seja 610 por exemplo
        return centenas[f'{frst_index_num}'] + ' e ' + dezenas[f'{middle_index_num}']

    elif dezena_ > 10 and dezena_ < 20: # caso seja 715 por exemplo
        if frst_index_num + middle_index_num + last_index_num == strnum:
            return centenas[f'{frst_index_num}'] + ' e ' + dez_ate_20[f'{str(dezena_)}']

    elif frst_index_num + middle_index_num + last_index_num == strnum: # caso a dezena seja maior que 19, 820 por exemplo
        return centenas[f'{frst_index_num}'] + ' e ' + dezenas[f'{middle_index_num}'] + ' e ' + unidade[f'{last_index_num}']

    

def converte(strnum):
    tamnum = len(strnum)
    if tamnum == 3:
        return converte_centena(strnum[0], strnum[1], strnum[2], strnum)
    elif tamnum == 2:
        return converte_dezena(strnum[0], strnum[1], strnum)
    elif tamnum == 1:
        return converte_unidade(strnum)

        
    



