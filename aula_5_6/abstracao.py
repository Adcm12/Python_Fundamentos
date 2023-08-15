from abc import ABC, abstractmethod

class PessoaAbstrata(ABC):

    @abstractmethod
    def gastar_dinero():        
        pass


    @abstractmethod
    def respirar():
        pass


    @abstractmethod
    def falar():
        pass


class Atleta(PessoaAbstrata):

    def gastar_dinero():

        print('Yo gasto poco dinero')


    def falar():

        print('Queremos un aumento')

    def respirar():

        print('Yo gano por respirar')


class Artista(PessoaAbstrata):

    def gastar_dinero():
    
        print('Yo gasto mucho dinero porque yo puedo')

    def falar():

        print('Yo soy rico y hablo 5 idiomas')

    def respirar():

        print('Estoy respirando')


Artista.gastar_dinero()
Atleta.gastar_dinero()
Atleta.falar()
Artista.falar()
Atleta.respirar()
Artista.respirar()

