# Meu primeiro programa
# Marco Antonio do Rosário <marcoantonio.1info@gmail.com

from random import randint  # Importa a função de gerar números aleatórios

print("Jogo dos dados: ")

dado1 = randint(1, 6)  # gera um número entre 1 e 6 aleatoriamente
print("Dado 1: ", dado1)

dado2 = randint(1, 6)  # gera um número entre 1 e 6 aleatoriamente
print("Dado 2: ", dado2)

dado3 = randint(1, 6)  # gera um número entre 1 e 6 aleatoriamente
print("Dado 3: ", dado3)

dado4 = randint(1, 6)  # gera um número entre 1 e 6 aleatoriamente
print("Dado 4: ", dado4)

jogador1 = dado1 + dado2
jogador2 = dado3 + dado4

print('Jogador 1: ', jogador1)
print('Jogador 2: ', jogador2)

if jogador1 > jogador2:
    print("Jogador 1 venceu!")
else:
    if jogador2 > jogador1:
        print("Jogador 2 venceu!")
    else:
        print("Empate!")







