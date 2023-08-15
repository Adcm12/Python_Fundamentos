# Crie uma classe Banco com métodos abstratos depositar(), ver_saldo() e sacar() e 
#     implemente a lógica de cada método. Crie subclasses ContaCorrente e ContaPoupanca
#     que herdam da classe Banco e implementam os métodos de acordo com suas regras específicas.
#     Por exemplo, a subclasse ContaPoupanca pode nao deter o método sacar().
#     Crie atributos privados e publicos nas subclasses ContaCorrente e ContaPoupanca
#     como self.nome, self.saldo, e self.numero_conta por exemplo. Crie objetos dessas
#     classes com informações distintas, invoque os métodos e printe o resultado das
#     operações. 

from abc import ABC, abstractmethod

class Banco():

    @abstractmethod
    def depositar(self):
        pass


    @abstractmethod
    def ver_saldo(self):
        pass

    @abstractmethod
    def sacar(self):
        pass


class ContaPopança(Banco):

    def __init__(self, nome, saldo, numero_conta):

        self.__nome = nome
        self._saldo = saldo
        self.numero_conta = numero_conta


    def depositar(self, dinero):

        print(f'\nUsted depositó {dinero}$ correctamente!!!')


    def intereses(self, dinero):

        interes = 0.1
        print(f'\nGanara un 10% por cada deposito recibido. \nPor el deposito de {dinero} recibira: {(dinero * interes)}')


    @property
    def ver_saldo(self):
        print(f'\nTitular: {self.__nome} \nSaldo: {self._saldo} \nNumero de cuenta: {self.numero_conta}')


    def sacar(self):
        print(f'\nEn la cuenta Poupança no puede hacer retiros!!!')


class ContaCorrente(Banco):

    def __init__(self, nome, saldo, numero_conta):

        self.__nome = nome
        self._saldo = saldo
        self.numero_conta = numero_conta


    def depositar(self, dinero):
        print(f'\nUsted depositó {dinero}$ correctamente!!!')

    def cartao_credito(self, limite):

        print(f'Usted tiene un cartao de credito de {limite}')

    @property
    def ver_saldo(self):
        print(f'\nTitular: {self.__nome} \nSaldo: {self._saldo} \nNumero de cuenta: {self.numero_conta}')


    def sacar(self, dinero):
        print(f'\nUsted retiro {dinero}$ correctamente!!!')    


pessoa1 = ContaPopança('Adrian Castillo', 1500, 524987)

pessoa1.ver_saldo
pessoa1.depositar(1500)
pessoa1.sacar()
pessoa1.intereses(1500)


pessoa2 = ContaCorrente('David Marcano', 500, 618463)

pessoa2.ver_saldo
pessoa2.cartao_credito(500)
pessoa2.depositar(200)
pessoa2.sacar(666)


