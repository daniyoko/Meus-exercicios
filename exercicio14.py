numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dez = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezenas = ('','','vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
definir = input('Informe um número de 0 a 99: ')
valor = int(definir)
if valor < 10:
    extenso = numero[valor]
elif valor <= 19:
    extenso = dez[valor-10]
else:
    numeral = ''
    if definir[1:2]!='0':
        numeral = ' e ' + numero[int(definir[1:2])]
    extenso = dezenas[int(definir[0:1])] + numeral
print(extenso)