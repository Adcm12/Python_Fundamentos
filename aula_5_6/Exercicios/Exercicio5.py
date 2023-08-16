# Crie uma classe Alimento com atributos como nome e calorias. Crie subclasses Fruta, Legume
# e Carne que herdam de Alimento e implementam seus próprios atributos. Crie uma função que aceita 
# uma lista de alimentos e calcula o total de calorias usando polimorfismo. Para mais precisão no
# exercício, é ideal pesquisar as calorias dos alimentos e criar objetos das subclasses com seus 
# respectivos construtores e atributos.

from abc import ABC, abstractmethod

class Alimento:

    def __init__(self, nome, calorias):

        self.nome = nome
        self.calorias = calorias

    @abstractmethod
    def mostrar(self):
        pass

class Fruta(Alimento):

    def __init__(self, nome, calorias, tipo):

        self.nome = nome
        self.calorias = calorias
        self.tipo = tipo
    
    def mostrar(self):

        print(f'\nNome: {self.nome} \nCalorías: {self.calorias} \nTipo: {self.tipo} ')

class Legume(Alimento):

    def __init__(self, nome, calorias, cor):

        self.nome = nome
        self.calorias = calorias
        self.cor = cor

    def mostrar(self):

        print(f'\nNome: {self.nome} \nCalorías: {self.calorias} \nCor: {self.cor} ')


class Carne(Alimento):
    def __init__(self, nome, calorias, tipo_carne):

        self.nome = nome
        self.calorias = calorias
        self.tipo_carne = tipo_carne

    def mostrar(self):

        print(f'\nNome: {self.nome} \nCalorías: {self.calorias} \nTipo: {self.tipo_carne} ')


def calcular_total_calorias(alimentos):

    total_calorias = 0

    for alimento in alimentos:

        total_calorias += alimento.calorias

    return total_calorias


fruta1 = Fruta("Maçã", 52, "Cítrica")
legume1 = Legume("Brócolis", 55, "Verde")
carne1 = Carne("Frango", 165, "Branca")

fruta1.mostrar()
legume1.mostrar()
carne1.mostrar()

alimentos = [fruta1, legume1, carne1]

total_calorias = calcular_total_calorias(alimentos)
print("\nTotal de calorias:", total_calorias)
