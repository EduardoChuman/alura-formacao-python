import random
print("{:*^60}" .format("*"))
print("{:*^60}" .format(" Bem-vindo ao jogo de Adivinhação! "))
print("{:*^60}" .format("*"))
print(" ")

numero_secreto = random.randrange(1, 101)
continua = 0
tentativa = 1
while continua == 0:
    print("Tentativa {}" .format(tentativa))
    tentativa = tentativa + 1
    chute = int(input("Digite o seu número (entre 1 e 100): "))
    print("Você digitou o número {}" .format(chute))

    if chute < 1 or chute > 100:
        print("Número digitado deve estar entre 1 e 100!")
        continue

    acertou     = numero_secreto == chute
    chute_maior = numero_secreto < chute
    chute_menor = numero_secreto > chute

    if acertou:
        print("Acertou!")
        break
    else:
        if chute_menor:
            print("Errou! Seu chute foi abaixo do número secreto")
            print(" ")
        elif chute_maior:
            print("Errou! Seu chute foi acima do número secreto")
            print(" ")

print(" ")
print("{:*^60}" .format("*"))
print("{:*^60}" .format(" Fim! "))
print("{:*^60}" .format("*"))
