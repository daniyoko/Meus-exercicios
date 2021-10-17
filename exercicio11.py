multiplicador = input('Informe um numero\t')
if (multiplicador.isnumeric()):
    for i in range(11):
        print('{} * {: >2} = {: >2}' .format(multiplicador, i, i * int(multiplicador)))