# Crie uma classe chamada ContaBancaria, com os atributos saldo (private), titular (public), 
# numero_conta (private). Crie métodos get_saldo() e set_saldo(novo_saldo) para acessar e modificar o saldo.

class ContaBancaria():

    def __init__(self, saldo, titular, numeroConta):

        self.titular = titular
        self._numeroConta = numeroConta
        self.__saldo = saldo

    @property
    def get_saldo(self):

        return f'\nSaldo:  {self.__saldo}'
    
    
    @get_saldo.setter
    def saldoo(self, saldo_novo):

        print(f'\nSetou de {self.__saldo}, para {saldo_novo}')
        self.__saldo = saldo_novo

if __name__=='__main__':

    saldo1 = ContaBancaria(1500, 'Adrian', 156498 )
    print(saldo1.get_saldo)

    saldo1.saldoo = 5000
    print(saldo1.saldoo)