import random

def jogar():
    
    montar_mensagem_abertura()
    palavra_secreta = define_palavra_secreta()
    lista_palavra_secreta = monta_mascara_palavra_secreta(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        print(" ")
        print(f"Palavra secreta : {lista_palavra_secreta}")
        chute = input("Informe uma letra: ").lower().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    lista_palavra_secreta[index] = letra.upper()                    
                index += 1
            if '_' in lista_palavra_secreta:
                letras_restantes = lista_palavra_secreta.count('_')
                print(f"Ainda falta descobrir {letras_restantes} letras")
                continue
            else:
                print(" ")
                print(f"Palavra secreta : {lista_palavra_secreta}")
                imprime_mensagem_vencedor()
                acertou = True
                break
        else:
            erros += 1
            desenha_forca(erros)
            if erros == 6:
                enforcou = True
                print("Puxa, você foi enforcado!")
                print("A palavra era {}".format(palavra_secreta))
            else:
                print(f"Ops, você errou! Faltam {6 - erros} tentativas.")

    montar_mensagem_final()


def montar_mensagem_abertura():
    print("{:*^60}" .format("*"))
    print("{:*^60}" .format(" Bem-vindo ao jogo de Forca! "))
    print("{:*^60}" .format("*"))
    print(" ")

def montar_mensagem_final():
    print(" ")
    print("{:*^60}".format("*"))
    print("{:*^60}".format(" Fim! "))
    print("{:*^60}".format("*"))

def define_palavra_secreta():
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta

def monta_mascara_palavra_secreta(palavra_secreta):
    return ["_" for posicao in palavra_secreta]

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |      /     ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |      / \   ")


    if(erros == 5):
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |      / \   ")
        

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      / \   ")
        print(" |            ")

    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if __name__ == "__main__":
    jogar()