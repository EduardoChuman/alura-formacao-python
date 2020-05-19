def jogar():
    print("{:*^60}" .format("*"))
    print("{:*^60}" .format(" Bem-vindo ao jogo de Forca! "))
    print("{:*^60}" .format("*"))
    print(" ")

    palavra_secreta = "banana"
    lista_palavra_secreta = ["_" for posicao in palavra_secreta]
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
                print(f"Parabéns! Você acertou a palavra secreta '{palavra_secreta}'")
                acertou = True
                break
        else:
            erros += 1
            if erros == 6:
                enforcou = True
                print("Você se enforcou... Tente novamente")
            else:
                print(f"Ops, você errou! Faltam {6 - erros} tentativas.")

    print(" ")
    print("{:*^60}".format("*"))
    print("{:*^60}".format(" Fim! "))
    print("{:*^60}".format("*"))


if __name__ == "__main__":
    jogar()