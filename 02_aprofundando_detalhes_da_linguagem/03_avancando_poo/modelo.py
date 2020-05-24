class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome     = nome.title()
        self.ano        = ano
        self.duracao    = duracao
        self.__likes    = 0

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes
    
    def dar_likes(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome     = nome.title()
        self.ano        = ano
        self.temporadas = temporadas
        self.__likes    = 0

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes
    
    def dar_likes(self):
        self.__likes += 1


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_likes()
vingadores.nome = 'vingadores - end game'

print(f"Filme: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}")

supernatural = Serie("supernatural", 2005, 15)
supernatural.dar_likes()
supernatural.dar_likes()
print(f"Serie: {supernatural.nome} - Ano: {supernatural.ano} - Temporadas: {supernatural.temporadas} - Likes: {supernatural.likes}")