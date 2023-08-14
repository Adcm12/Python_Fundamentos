# Crie uma classe chamada Hotel. Defina um atributo nome (private) e estrelas (public). 
# Crie métodos get_nome(), set_nome(novo_nome) e get_estrelas() para acessar e modificar esses atributos.

class Hotel:

    def __init__(self, nome, estrelas):

        self.__nome = nome  
        self.estrelas = estrelas  

    def get_nome(self):

        return f'\nNome do hotel: {self.__nome}'
    

    def set_nome(self, novo_nome):

        self.__nome = novo_nome
        print(f'\nNovo nome do hotel: {novo_nome}')


    def get_estrelas(self):

        return f'\nEstrelas: {self.estrelas}'


meu_hotel = Hotel("Hotel Bela Vista", 4)


print(meu_hotel.get_nome())


print(meu_hotel.get_estrelas())


meu_hotel.set_nome("Hotel Luxuoso")

