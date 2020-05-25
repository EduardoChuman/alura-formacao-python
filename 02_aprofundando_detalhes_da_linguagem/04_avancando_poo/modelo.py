class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1
    
    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}"

    # def imprimir(self):
    #     print(f"Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}")


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao    = duracao
    
    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} minutos - Likes: {self._likes}"

    # def imprimir(self):
    #     print(f"Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} minutos - Likes: {self._likes}")


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Duração: {self.temporadas} temporada(s) - Likes: {self._likes}"
    
    # def imprimir(self):
    #     print(f"Nome: {self._nome} - Ano: {self.ano} - Duração: {self.temporadas} temporada(s) - Likes: {self._likes}")

# # Playlist sem herança
# class Playlist:
#     def __init__(self, nome, programas):
#         self.nome       = nome
#         self.programas  = programas
    
#     def tamanho(self):
#         return len(self.programas)

# # Playlist com herança
# class Playlist(list):
#     def __init__(self, nome, programas):
#         self.nome       = nome
#         super().__init__(programas)

# Playlist sem herança e com alteracoes de atributos e métodos
class Playlist:
    def __init__(self, nome, programas):
        self.nome       = nome
        self._programas  = programas

    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas
    


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_likes()

spider_man = Filme("Homen Aranha", 2016, 109)
spider_man.dar_likes()
spider_man.dar_likes()
spider_man.dar_likes()

mr_robbot = Serie("Mr. Robbot", 2016, 4)
mr_robbot.dar_likes()
mr_robbot.dar_likes()
mr_robbot.dar_likes()
mr_robbot.dar_likes()
mr_robbot.dar_likes()
mr_robbot.dar_likes()

supernatural = Serie("supernatural", 2005, 15)
supernatural.dar_likes()
supernatural.dar_likes()

lista_filmes_e_series = [vingadores, supernatural, mr_robbot, spider_man]
playlist_final_de_semana = Playlist("Playlist de Final de Semana", lista_filmes_e_series)

# # Primeira Forma: Com uso de operador ternário e hasattr
# for programa in lista_filmes_e_series:
    # detalhes = f"{programa.temporadas} temporadas" if hasattr(programa, 'temporadas') else f"{programa.duracao} minutos"
    # print(f"Nome: {programa.nome} - Ano: {programa.ano} - Duração: {detalhes} - Likes: {programa.likes}")
    
# # Segunda Forma: Com poliformismo do método imprimir
# for programa in lista_filmes_e_series:
    # programa.imprimir()

# # Terceira Forma: Com uso de método mágico __str__ (semelhante ao toString() do PHP) 
# for programa in lista_filmes_e_series:
    # print(programa)

# # Usando a classe Playlist (Sem herança)
# print(f"Tamanho da playlist: {playlist_final_de_semana.tamanho} programas")
# for programa in playlist_final_de_semana.listagem:
#     print(programa)

# # Usando a classe Playlist (Com herança)
# print(f"Tamanho da playlist: {len(playlist_final_de_semana)} programas")

# for programa in playlist_final_de_semana:
#     print(programa)

# Usando a classe Playlist (Sem herança, mas com método mágico que "usa" atributos de outro objeto - Duck Type)
print(f"Tamanho da playlist: {len(playlist_final_de_semana)} programas")
for programa in playlist_final_de_semana:
    print(programa)




