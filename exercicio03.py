'''Programa para calcular dois numeros

'''
#Calculadora simples
print('Vamos fazer a soma de dois números inteiros')
num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')
print('O primeiro numero é {} e o segundo numero é {}' . 
    format(num1, num2))
soma = num1 + num2
#não precisa declarar variavel
print('A soma dos dois números é {} ' . format(soma))
#coloca  a chave para retornar um valor e usa o . format, 
print('O tipo de dados dos números é {}' . format(type(num1)))
soma = int(num1) + int(num2)
print('A soma correta é {}' . format(soma))
#para numeros com clasa decimal usar o coando float
#peça novamente dois numeros com casas decimais e faça a soma
num1 = float(input('Informe um número com casas decimais: '))
num2 = float(input('Informe um número com casas decimais: '))
somaf = num1 + num2
print('A soma dos numeros com casas decimais é {}' . format(somaf))