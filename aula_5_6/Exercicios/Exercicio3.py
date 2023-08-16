# Crie uma classe base Veiculo com atributos como marca, modelo e métodos como ligar()
# e desligar(), entre outros. Crie as subclasses Carro e Moto que herdam de Veiculo e
# implementam seus próprios métodos beaseando-se na abstratação de Veiculo. Em seguida,
# crie uma classe Garagem que aceita veículos e gerencia o estacionamento usando herança.
# Crie e trabalhe com os getters e setters para a classe Garagem.

import time 
from abc import ABC, abstractmethod

class Vehiculo():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Vehiculo):


    def ligar(self):

        if not self.ligado:

            self.ligado = True

            time.sleep(1.5)

            print(f'\n\U0001F697 {self.marca} {self.modelo} ligo com sucesso!')

        else:
            print(f'\n\U0001F697 {self.marca} {self.modelo} ja esta ligado!\n')

    def desligar(self):

        if self.ligado:

            self.ligado = False

            time.sleep(1.5)

            print(f'\n\U0001F697 {self.marca} {self.modelo} desligou con sucesso!')

        else:
            print(f"\n\U0001F697 {self.marca} {self.modelo} já está desligado!")


class Moto(Vehiculo):


    def ligar(self):

        if not self.ligado:

            self.ligado = True

            time.sleep(1.5)

            print(f'\n\U0001F3CD {self.marca} {self.modelo} ligo com sucesso!')

        else:
            print(f'\n\U0001F3CD {self.marca} {self.modelo} ja esta ligada!\n')

    def desligar(self):

        if self.ligado:

            self.ligado = False

            time.sleep(1.5)

            print(f'\n\U0001F3CD {self.marca} {self.modelo} desligou con sucesso!')

        else:
            print(f"\n\U0001F3CD {self.marca} {self.modelo} já está desligada!")


class Garagem:

    def __init__(self):

        self._veiculos = []
        
    def adicionar_veiculo(self, veiculo):

        self._veiculos.append(veiculo)
        print(f"\n\U0001F512 {veiculo.marca} {veiculo.modelo} estacionado(a) na garagem.")
        
    def remover_veiculo(self, veiculo):

        self._veiculos.remove(veiculo)
        print(f"\n\u274C {veiculo.marca} {veiculo.modelo} removido(a) da garagem.")
        
    def listar_veiculos(self):

        if len(self._veiculos):

            print("\n\U0001F4CB Veículos na garagem:")

            for veiculo in self._veiculos:
                print(f"\n  \u2714 {veiculo.marca} {veiculo.modelo}")
        
        else: 

            print('El garagem esta vacio')
            

    @property
    def veiculos(self):

        return self._veiculos
    
    @veiculos.setter
    def veiculos(self, veiculos):

        self._veiculos = veiculos




carro1 = Carro('Masserati', 'Granturismo')

carro1.ligar()
carro1.desligar()

moto1 = Moto('Honda', 'CB 500X')

moto1.ligar()
moto1.desligar()

garagem = Garagem()
garagem.adicionar_veiculo(carro1)
garagem.adicionar_veiculo(moto1)
garagem.listar_veiculos()

garagem.remover_veiculo(carro1)
garagem.listar_veiculos()
