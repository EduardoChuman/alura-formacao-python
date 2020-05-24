import adivinhacao_niveis_dificuldade
import forca

def define_jogo():
    print("{:*^60}" .format("*"))
    print("{:*^60}" .format(" Bem-vindo a lista de jogos! "))
    print("{:*^60}" .format("*"))
    print(" ")

    print("Escolha o jogo que você deseja jogar:")
    print("(1) Adivinhaçāo - (2) Forca")
    codigo_jogo = int(input("Digite o número do jogo: "))
    print(" ")

    if codigo_jogo == 1:
        adivinhacao_niveis_dificuldade.jogar()
    elif codigo_jogo == 2:
        forca.jogar()


if __name__ == '__main__':
    define_jogo()
