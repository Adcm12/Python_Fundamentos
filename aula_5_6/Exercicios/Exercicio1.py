# 1 - Crie uma classe abstrata chamada Animal com métodos falar(), comer() e mover().
#     Crie subclasses Cachorro, Cavalo e Gato que herdam da classe Animal e implementam
#     seus próprios métodos, printando frases diferentes.  
#     Crie e trabalhe com os getters e setters para as subclasses.

from abc import ABC, abstractmethod

class Animal():

    def __init__(self, especie, edad, peso, cor):

        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.cor = cor


    @abstractmethod
    def falar(self):
        pass


    @abstractmethod
    def comer(self):
        pass


    @abstractmethod
    def mover(self):
        pass


    @abstractmethod
    def exibir_informaciones(self):
        
        print(f'\nEspecie: {self.especie} \nEdad: {self.edad} \nPeso: {self.peso} \nCor: {self.cor}')



class Cavalo(Animal):

    
    def emitit_som(self):

        print('\U0001F434 Prusfksjadks')

    
    def comer(self):

        print('\U0001F434 Yo estoy comiendo')

    
    def mover(self):

        print('\U0001F434 Yo estoy corriendo')


    def exibir_informaciones(self):
        
        print(f'\nEspecie: {self.especie} \nEdad: {self.edad} \nPeso: {self.peso} \nCor: {self.cor}')


class Cachorro(Animal):


    def emitit_som(self):

        print('\U0001F436 uau uau uau')

    
    def comer(self):

        print('\U0001F436 Yo estoy comiendo perrarina')

    
    def mover(self):

        print('\U0001F436 Yo estoy corriendo atras del carro')

    def exibir_informaciones(self):
        
        print(f'\nEspecie: {self.especie} \nEdad: {self.edad} \nPeso: {self.peso} \nCor: {self.cor}')


class Gato(Animal):

    def emitit_som(self):

        print('\U0001F63A miau miau')

    
    def comer(self):

        print('\U0001F63A Yo estoy comiendo pescado')

    
    def mover(self):

        print('\U0001F63A Yo estoy jugando con la luz')

    def exibir_informaciones(self):
        
        print(f'\nEspecie: {self.especie} \nEdad: {self.edad} \nPeso: {self.peso} \nCor: {self.cor}')



cavalo1 = Cavalo('Machador', 19, 120, 'Marron')
cavalo2 = Cavalo('Machador', 10, 80, 'Preto')

cavalo1.exibir_informaciones()
cavalo1.comer()
cavalo1.falar()
cavalo2.exibir_informaciones()
cavalo2.comer()
cavalo2.falar()


gato1 = Gato('Calvo', 5, 6, 'Cinza')

gato1.exibir_informaciones()
gato1.comer()
gato1.falar()

cacho = Cachorro('Pitbull', 5, 80, 'Preto')

cacho.exibir_informaciones()
cacho.comer()
cacho.falar()