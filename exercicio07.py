from os import system, name
if (name == 'nt'):
    system('cls')
else:
    system('clear')
número = int(input('Informe um numero: '))
resultado = int(número %2)
print(resultado)
if resultado == 0: 
    print('O numero é par')
else:
    print('O numero é impar')
print('Final do código')

