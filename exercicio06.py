nomecompleto = 'Daniele Yoko Tokimatu 4'
print(nomecompleto.isalnum()) #nao pode ter espaço em branco, senao nao identifica
print(nomecompleto.isalpha())
print(nomecompleto.replace(' ', '').isalpha())
print(nomecompleto.upper()) #transforme em maiusculo
print(nomecompleto.lower()) #minusculo
print(nomecompleto.capitalize()) #primeira maiuscula 
print(len(nomecompleto))
print(nomecompleto[0:7]) #pega os caracteres de acordo com o escolhido, a prtir do zero, pega ate o setimo.
print(nomecompleto[8:-1]) #pega a partir do caractere oito, ate o penultimo
print(nomecompleto.center(80, "*"))
print(nomecompleto.split(" ")) #separa as palavras