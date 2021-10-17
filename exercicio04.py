from os import system, name #importar biblioteca
system('cls') if(name == 'nt') else system ('clear')  #widndows, se for linux é clear
print('Vamos calcular a área do retangulo')
lado1 = input('Informe o primeiro lado do retangulo\t')
lado2 = input('Informe o segundo lado do retangulo\t')
#print('O lado 1 é {} e o lado 2 é {}' . format(lado1, lado2))
print(type(lado1))
#int isnumeric() e float = isdecimal()
print('Lado 1 é numero? {}' .format(lado1.isnumeric())) #metodos tem que colocar parenteses (desenho do cubo)
print('Lado 2 é numero? {}' .format(lado2.isnumeric()))
area = float(lado1) * float(lado2)
print('A area do retangulo é {}' .format(area))
print(type(area))
