import random

jogador = int(input(''''Escolha uma opção oara se jogar:
[0] Pedra
[1] Papel
[2] Tesoura
Digite sua escolha: '''))
computador = random.randint(0,2)

pecas = ["Pedra", "Papel", "Tesoura"]
result = [[0, -1, 1],[1, 0, -1],[-1, 1, 0]]
#print(result[])
print('Voce escolheu {}' .format(pecas[jogador]))
print(computador, ' - ', jogador)
print('O computador escolheu: {}' .format(pecas[computador]))

r = result[computador][jogador]
if r == 0:
    resultado = "Deu empate, vocês ecolheram a mesma peça"
elif r == 1:
    resultado = "O computador ganhou!"
else:
    resultado = "Voce ganhou"

print(resultado)