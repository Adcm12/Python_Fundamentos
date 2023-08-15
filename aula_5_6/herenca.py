# Parent class

class Animal():

    def __init__(self, nome, cor):

        self.nome = nome
        self.cor = cor


    def correr(self):

        print(f'\U0001F1E6 {self.nome} esta correndo')


    def comer(self):

        print(f'\U0001F1E6 {self.nome} se esta alimentando')


# SubClass heredando clase animal

class Cachorro(Animal):

    def latir(self):

        print('\U0001F436 auauauaua')

class Gato(Animal):

    def destruir_sofa(self):

        print('\U0001F63A Su sofa fue destruido')
    
    def miar(self):

        print('\U0001F63A meau meau')


cacho = Cachorro('Pitbull', 'Black')

cacho.comer()
cacho.correr()
cacho.latir()

gato = Gato ('Calvo', 'Cinza')

gato.comer()
gato.destruir_sofa()
gato.miar()