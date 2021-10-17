print('*** CONVERSOR DE TEMPERATURA ***')
print('\nEscolha uma das opções\n', '1 - Converter de Celsius para Fahrenheit\n', '2 - Converter de Fahrenheit para Celsius\n\n')
menu = int(input('Opção: '))
print('\n')
temperatura = float(input('Agora informe a temperatura: '))
if menu==1:
  resultado = (temperatura * 9 / 5) + 32
  print("{:.2f} Celsius corresponde a {:.2f} Fahrenheit".format(temperatura, resultado))
else:
  resultado = (temperatura - 32) * 5 / 9
  print("{:.2f} Fahrenheit corresponde a {:.2f} Celsius".format(temperatura, resultado))