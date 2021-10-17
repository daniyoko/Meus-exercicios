peso = 61
altura = 1.47
print(type(altura))#uo o type pra saber o tipo, string, numero etc
imc = peso / (altura * altura)
print('O seu IMC é de {:.2f}' .format(imc))
if (imc < 18.5):
    resultado = 'Abaixo do peso'
elif (imc < 25):
    resultado = 'Peso Normal'
elif(imc < 30):
    resultado = 'Sobrepeso'
else:
    resultado = 'Obesidade'
print(resultado)