import random

def jogar():
    print("{:*^60}".format("*"))
    print("{:*^60}".format(" Bem-vindo ao jogo de Adivinhação! "))
    print("{:*^60}".format("*"))
    print(" ")

    numero_secreto = random.randrange(1, 101)
    chances = 0
    pontos = 100

    while chances == 0:
        print("Níveis de dificultade:")
        print("(1) Fácil - (2) Médio - (3) Difícil")
        nivel = int(input("Informe o nível de dificuldade você deseja: "))

        if nivel < 1 or nivel > 3:
            print("Nāo foi reconhecido o nível informado. Tente novamente!")
            print(" ")
            continue
        elif nivel == 1:
            chances = 20
            print(" ")
        elif nivel == 2:
            chances = 10
            print(" ")
        else:
            chances = 5
            print(" ")

    for tentativa in range(1, chances + 1):
        print("Tentativa {} de {}".format(tentativa, chances))

        chute = int(input("Digite o seu número (entre 1 e 100): "))
        print("Você digitou o número {}".format(chute))

        if chute < 1 or chute > 100:
            print("Número digitado deve estar entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        chute_maior = numero_secreto < chute
        chute_menor = numero_secreto > chute

        if acertou:
            print("Acertou!")
            print(f"Você fez {pontos} pontos")
            break
        else:
            if chute_menor:
                print("Errou! Seu chute foi abaixo do número secreto")
                print(" ")
            elif chute_maior:
                print("Errou! Seu chute foi acima do número secreto")
                print(" ")
            pontos_perdidos = 100 / chances
            pontos = int(pontos - pontos_perdidos)

    print(" ")
    print("{:*^60}".format("*"))
    print("{:*^60}".format(" Fim! "))
    print("{:*^60}".format("*"))


if __name__ == "__main__":
    jogar()