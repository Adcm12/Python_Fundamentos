# Crie uma classe abstrata Animal com um método emitir_som(). Crie subclasses Cachorro,
#     Gato, Cavalo e Vaca que herdam de Animal e implementam seus próprios sons. Crie uma função
#     que aceita uma lista de animais e faça-os emitir sons usando polimorfismo.
#     Em seguida, crie contrutores para as subclasses dando um atributo nome e cor, e crie
#     objetos dessas subclasses com cores e nomes distintos.

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        
    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def imformacion(self):
        pass

class Cachorro(Animal):

    def emitir_som(self):
        return "\U0001F436 Cachorro: au au au au"

    def imformacion(self):

        print(f'\n\U0001F436 Cachorro \nNome: {self.nome} \nCor: {self.cor}')

class Gato(Animal):

    def emitir_som(self):
        return "\U0001F408 Gato: meau meau"
    
    def imformacion(self):

        print(f'\n\U0001F408 Gato \nNome: {self.nome} \nCor: {self.cor}')

class Cavalo(Animal):

    def emitir_som(self):
        return "\U0001F40E Cavalo: Prfmksaijsodas"

    def imformacion(self):

        print(f'\n\U0001F40E Cavalo \nNome: {self.nome} \nCor: {self.cor}')

class Vaca(Animal):

    def emitir_som(self):
        return "\U0001F404 Vaca: Muuuu"
    
    def imformacion(self):

        print(f'\n\U0001F404 Vaca \nNome: {self.nome} \nCor: {self.cor}\n')

def fazer_sons(animais):

    for animal in animais:
        print(animal.emitir_som())


cachorro = Cachorro("Oslo", "Marrom")
gato = Gato("Mr gato", "Branco")
cavalo = Cavalo("Split", "Preto")
vaca = Vaca("Lola", "Malhada")

cachorro.imformacion()
gato.imformacion()
cavalo.imformacion()
vaca.imformacion()


animais = [cachorro, gato, cavalo, vaca]


fazer_sons(animais)
