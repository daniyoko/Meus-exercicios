def soma(n1,n2):
    print('Soma: {}' .format(n1+n2))
def subtracao(n1,n2):
    print('Subtração: {}' .format(n1-n2))
def divisao(n1,n2):
    print('Divisão: {}' .format(n1/n2))
def multiplicao(n1,n2):
    print('Multiplicação: {}' .format(n1*n2))

opcao = 1
while opcao: 
    print('[0] Sair')
    print('[1] Calcular')
    opcao = int(input('Escolha uma das opções: '))
    if opcao == 1:
        num1 = float(input('Primeiro numero: '))
        num2 = float(input('Segundo numero: '))
        print('1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir')
        operador = int(input('Escolha o operador: '))
        if(operador==1):
            soma(num1,num2)
        elif(operador==2):
            subtracao(num1,num2)
        elif(operador==3):
            multiplicao(num1,num2)
        elif(operador==4):
            divisao(num1,num2)
        else:
            print('Escolha de 1 a 4')